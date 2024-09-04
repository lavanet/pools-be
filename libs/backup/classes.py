from os import path, remove
from subprocess import run

from django.conf import settings
from django.utils.timezone import now

from libs.utils import logger


class TmpFile(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        return self.filepath

    def __exit__(self, *args):
        try:
            remove(self.filepath)
        except:
            logger.error('Failed to remove temporary PgDump file [%s]', self.filepath)


class PgDump(object):
    def __init__(self, directory, name_frmt, cmd):
        self.directory = directory
        self.name_frmt = name_frmt
        self.cmd = cmd
        self.base_args = ('pg_dump',) + cmd

    def create(self):
        filepath = path.join(self.directory, now().astimezone().strftime(self.name_frmt))
        run(
            args=self.base_args + (f'--file={filepath}',),
            cwd=settings.BASE_DIR,
            check=True,
        )
        return TmpFile(filepath)


class S3Bucket(object):
    def __init__(self, name):
        self.url = f's3://{name}'
        self.base_args = 'aws', 's3',

    def __call__(self, *args, **kwargs):
        cp = run(
            args=self.base_args + tuple(args),
            cwd=settings.BASE_DIR,
            check=True,
        )
        return cp

    def join_prefix(self, prefix=None):
        retval = self.url
        if prefix:
            retval = '/'.join((retval, prefix.strip('/') + '/'))
        return retval

    def ls(self, prefix=None):
        return self('ls', self.join_prefix(prefix))

    def assert_bucket(self):
        return self('mb', self.url)

    def cp(self, source, destination=None):
        return self('cp', source, self.join_prefix(destination))

    def sync(self, source, destination=None):
        return self('sync', '--size-only', source, self.join_prefix(destination))

    def get(self, prefix):
        return self('get', self.join_prefix(prefix))
