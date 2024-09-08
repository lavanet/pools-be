# coding: UTF-8
from os import path, environ
from dotenv import load_dotenv

load_dotenv()

ENV = 'dev'
INSTALLED_APPS = (
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # SITE-PACKAGE
    'debug_toolbar',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'test_without_migrations',

    # LIBS
    'libs.admin_register',
    'libs.emails',
    'libs.log_tailer',
    'libs.startup',

    # APPS
    'apps.api',
    'apps.api.api_auth',
    'apps.core',
    'apps.core.blockchains',
    'apps.core.coingecko',
    'apps.core.lava_queries',
    'apps.core.users',
)

ADMINS = (
    ('William', 'william@webisoft.com'),
    ('snickk', 'simon@webisoft.com'),
)

LOGIN_URL = 'admin:index'

PROJECT_SETTINGS = path.dirname(__file__)
BASE_DIR = path.dirname(PROJECT_SETTINGS)
SITE_ID = 1

DEBUG = True
ALLOWED_HOSTS = '*',

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

TIME_ZONE = 'US/Eastern'
USE_I18N = True
USE_L10N = True
USE_TZ = True

WSGI_APPLICATION = 'config.wsgi.application'

ROOT_URLCONF = 'config.urls'
STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')
FIXTURE_DIRS = 'fixtures/',
LOCALE_PATHS = 'locale/',
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap4',)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": environ.get("POSTGRES_DB", 'vagrant'),
        "USER": environ.get("POSTGRES_USER", 'vagrant'),
        "PASSWORD": environ.get("POSTGRES_PASSWORD", 'a'),
        "HOST": environ.get("POSTGRES_HOST", 'localhost'),
        "PORT": environ.get("POSTGRES_PORT", 5432),
        'CONN_MAX_AGE': 30,
        'OPTIONS': {
            'sslmode': 'disable',
        },
    },
}

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ('templates/',),
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
            ),
            'loaders': (
                'django.template.loaders.app_directories.Loader',
            )
        },
    },
)

MB = 2 ** 20

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
    },
    'formatters': {
        'simple': {'format': '[%(asctime)s] %(pathname)s (L: %(lineno)d); %(levelname)s: %(message)s'},
        'short': {'format': '[%(asctime)s] %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'},
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'short',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false', ],
        },
        'default_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/default.log',
            'maxBytes': 256 * MB,
            'backupCount': 3,
            'formatter': 'simple',
        },
        'api_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/api.log',
            'maxBytes': 50 * MB,
            'backupCount': 2,
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'propagate': True,
            'handlers': ['console', 'default_file', 'mail_admins', ],
        },
        'django.request': {
            'level': 'INFO',
            'propagate': False,
            'handlers': ['console', 'mail_admins', ],
        },
        'django.security.DisallowedHost': {
            'level': 'CRITICAL',
            'propagate': False,
            'handlers': ['console', 'default_file', 'mail_admins', ],
        },
        'default': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console', 'default_file', 'mail_admins', ],
        },
        'celery': {
            'level': 'INFO',
            'propagate': True,
            'handlers': ['console', 'mail_admins', ],
        },
        'apps.api': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console', 'api_file', ],
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
PROJECT_DOMAIN = 'http://localhost:8000'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'console@localhost'
BROKER_URL = 'redis://{hostname}:6379/0'.format(hostname=environ.get('REDIS_HOST', '127.0.0.1'))
CELERY_TIMEZONE = TIME_ZONE
CELERYD_HIJACK_ROOT_LOGGER = False
DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': 'config.debugtoolbar.show_toolbar'}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.cache.CachePanel',
)
SHOW_DEBUG_TOOLBAR = True
FILE_UPLOAD_PERMISSIONS = 0o644
DATA_UPLOAD_MAX_MEMORY_SIZE = None  # Limited by nginx.
SECURE_PROXY_SSL_HEADER = 'HTTP_X_FORWARDED_PROTO', 'https'
SPACE_DIRECTORIES = (
    # Directory, Threshold [0.00, 1.00]
    (BASE_DIR, 0.8),
    (MEDIA_ROOT, 0.8),
)
CUCUMBER_RATE_LIMIT = 5
CSRF_TRUSTED_ORIGINS = (
    'http://localhost:3000',
)

###############################################################################################
# Project specific  #
######################

PROJECT_NAME = 'lavapool'
SECRET_KEY = environ.get('DJANGO_SECRET_KEY', 'temporary_secret_key_for_dev')
AUTH_USER_MODEL = 'users.User'
STARTUP_INITIAL_FIXTURES = (
    'admins',
)

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'apps.api.handlers.exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'apps.api.pagination.Paginator',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

try:
    from .local_settings import *
except ImportError as e:
    if 'local_settings' not in str(e):
        raise
