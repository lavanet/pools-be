from django.conf import settings

get_or_def = lambda key, value: getattr(settings, key, value)

PG_DUMP_DIRECTORY = get_or_def('PG_DUMP_DIRECTORY', '/tmp')
PG_DUMP_FILE_FORMAT = get_or_def('PG_DUMP_CMD', 'pg.%Y-%m-%d-%Hh%M.db')
PG_DUMP_CMD = get_or_def('PG_DUMP_CMD', ('--format=custom',))
PG_RESTORE_CMD = get_or_def('PG_RESTORE_CMD', ('--clean',))

BACKUP_ENABLED = get_or_def('BACKUP_ENABLED', False)
BACKUP_CRONTAB = get_or_def('BACKUP_CRONTAB', {
    'minute': '0',
    'hour': '0',
})
