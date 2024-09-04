from celery.schedules import crontab
from celery.task import periodic_task
from django.conf import settings
from django.db import DataError
from django.db.utils import ConnectionDoesNotExist

from .classes import S3Bucket, PgDump
from .settings import PG_DUMP_FILE_FORMAT, PG_DUMP_CMD, \
    BACKUP_CRONTAB, PG_DUMP_DIRECTORY, BACKUP_ENABLED
from ..lockfile import Lockfile
from ..print_time import PrintTime
from ..utils import logger

bucket = S3Bucket(name=f'webisoft--{settings.PROJECT_NAME}--{settings.ENV}')

pg_dump = PgDump(
    directory=PG_DUMP_DIRECTORY,
    name_frmt=PG_DUMP_FILE_FORMAT,
    cmd=PG_DUMP_CMD,
)


@Lockfile(uid='backup.save_all.f90ri4n9ej3')
@PrintTime(output=logger.info)
def save_all():
    # bucket.assert_bucket()  # No permission to create bucket.
    save_db()
    save_media()


if BACKUP_ENABLED:
    save_all = periodic_task(run_every=crontab(**BACKUP_CRONTAB))(save_all)


@PrintTime(output=logger.info)
def save_db():
    with pg_dump.create() as filepath:
        bucket.cp(
            source=filepath,
            destination='database',
        )


@PrintTime(output=logger.info)
def save_media():
    bucket.sync(
        source=settings.MEDIA_ROOT,
        destination='media',
    )


def restore_db():
    bucket.ls('database')
    filepath = input('Enter the name of database to restore [ie: "pg.2020-07-22-15h25.db"]: ')
    print('Restoring:', filepath)


def shell():
    while 1:
        cmd = input()
        if not cmd:
            break
        bucket(*cmd.split(' '))


def get():
    with bucket.get('database/pg.2020-07-22-16h28.db') as filepath:
        pass


def remote_file():
    prefix = 'https-bidxpert.com/media/'
    import django.apps
    from django.db.models import FileField
    for model in django.apps.apps.get_models():
        filefields = tuple(
            field.name for field in model._meta.get_fields()
            if issubclass(type(field), FileField)
        )
        try:
            for obj in model.objects.all():
                for fieldname in filefields:
                    field = getattr(obj, fieldname)
                    if field:
                        filename = field.name
                        if not filename.startswith(prefix):
                            setattr(obj, fieldname, prefix + field.name)
                try:
                    obj.save(update_fields=filefields)
                except DataError as e:
                    logger.debug('Remote file error %s[%s]: %s', model.__qualname__, obj.pk, str(e))
        except ConnectionDoesNotExist:
            pass
