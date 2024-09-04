import hashlib
import os
from collections import OrderedDict
from logging import getLogger
from urllib.parse import urldefrag, urlsplit, unquote, urljoin

from django.contrib.staticfiles.storage import ManifestFilesMixin, StaticFilesStorage
from django.db.models import FileField
from django.db.models.signals import post_delete

_logger = getLogger('default')


class CacheBustingStaticFilesStorage(ManifestFilesMixin, StaticFilesStorage):
    """
    A simple static file storage that will create a manifest where hash for each files are stored.
    The manifest is created whe you do collect static. You need to restart app thereafter.
    It will add the hash to the end of the url to do cache busting
    """

    def post_process(self, paths, dry_run=False, **options):
        """
        Runs after collect static
        """
        if dry_run:
            return

        # where to store the new paths
        hashed_files = OrderedDict()

        # build a list of adjustable files
        # then sort the files by the directory level
        path_level = lambda name: len(name.split(os.sep))
        for name in sorted(paths.keys(), key=path_level, reverse=True):
            # use the original, local file, not the copied-but-unprocessed
            # file, which might be somewhere far away, like S3
            storage, _path = paths[name]

            with storage.open(_path) as original_file:
                # generate the hash with the original content, even for
                # adjustable files.
                _hash = self.hashed_name(name=name, content=original_file)

                # ..to apply each replacement pattern to the content
                # and then set the cache accordingly
                hashed_files[self.hash_key(name)] = _hash
                yield name, _hash, True

        # Finally store the processed paths
        self.hashed_files.update(hashed_files)
        self.save_manifest()

    def file_hash(self, name, content=None):
        """
        Returns a hash of the file with the given name and optional content.
        """
        if content is None:
            return None
        md5 = hashlib.md5()
        for chunk in content.chunks():
            md5.update(chunk)
        return md5.hexdigest()[:4]

    def hashed_name(self, name, content=None):
        parsed_name = urlsplit(unquote(name))
        clean_name = parsed_name.path.strip()
        return self.file_hash(clean_name, content)

    def url(self, name, force=False):
        """
        Returns the real URL in DEBUG mode.
        """
        hashed_name = None

        clean_name, fragment = urldefrag(name)
        if not urlsplit(clean_name).path.endswith('/'):  # don't hash paths
            hashed_name = self.stored_name(clean_name)

        if hashed_name:
            url = ''.join((clean_name, '?v=', hashed_name))
        else:
            url = name

        return urljoin(self.base_url, url)

    def stored_name(self, name):
        hash_key = self.hash_key(name)
        cache_name = self.hashed_files.get(hash_key)
        return cache_name


def remove_media(instance, logger=_logger, **kwargs):
    """
    Signal receiver for post_delete that
    will remove all files of FileFields in
    the instance.
    """
    for field in instance._meta.get_fields():
        if issubclass(type(field), FileField):
            info = instance.__class__.__qualname__, instance.pk, field.name,
            try:
                instance_field = getattr(instance, field.name)
                if instance_field:
                    instance_field.delete(save=False)
                    logger.debug('Media [%s:%s] deleted media [%s]' % info)
            except:
                logger.warning('Model [%s:%s] could not delete media [%s]' % info)


def remove_media_on_delete(klass):
    """
    Decorator to connect the remove_media
    receiver on a model class.
    """
    post_delete.connect(
        receiver=remove_media,
        sender=klass,
        dispatch_uid='%s-remove_media_on_delete' % klass.__qualname__,
    )
    return klass
