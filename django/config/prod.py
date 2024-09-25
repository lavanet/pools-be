from .secretsmanager import get_secret
from .settings import *  # noqa

DEBUG = False

SECRET_KEY = get_secret(environ.get('DJANGO_SECRETS'))['secretkey']
DB_SECRETS = get_secret(environ.get('DB_SECRETS'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_SECRETS['dbname'],
        'USER': DB_SECRETS['username'],
        'PASSWORD': DB_SECRETS['password'],
        'HOST': DB_SECRETS['host'],
        'PORT': DB_SECRETS['port'],
        'CONN_MAX_AGE': 30,
        'OPTIONS': {
            'sslmode': 'disable',
        },
    },
}

TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.app_directories.Loader',
    )),
)

STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3.S3Storage',
        'OPTIONS': {},
    },
    'staticfiles': {
        'BACKEND': 'storages.backends.s3.S3Storage',
        'OPTIONS': {},
    },
}

AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')
