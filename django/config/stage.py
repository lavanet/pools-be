from os import environ

ENV = 'stage'
DB_USER = 'lavapool'
DB_NAME = 'lavapool'
DB_PASS = environ.get('DJANGO_DB_PASS')
ALLOWED_HOSTS = (
    '*',  # tODO add prod IP here.
)
PROJECT_DOMAIN = 'http://127.0.0.1'  # tODO add prod IP here.

DEBUG = False
COMPRESS = True
PROJECT_NAME = 'lavapool'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': DB_USER,
        'NAME': DB_NAME,
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'CONN_MAX_AGE': 30,
        'OPTIONS': {
            'sslmode': 'disable',
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 300,
    },
    'redis': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/0',
        'TIMEOUT': 300,
        'KEY_PREFIX': 'django-%s-' % PROJECT_NAME,
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'redis'

STATICFILES_STORAGE = 'libs.storage.CacheBustingStaticFilesStorage'

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
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.app_directories.Loader',
                )),
            ),
        },
    },
)

EMAIL_BACKEND = 'libs.emails.backends.CelerySESBackend'
BASE_FROM_EMAIL = 'info@webisoft.org'
SERVER_EMAIL = f'{PROJECT_NAME}+stage <{BASE_FROM_EMAIL}>'
DEFAULT_FROM_EMAIL = f'{PROJECT_NAME}+stage <{BASE_FROM_EMAIL}>'
AWS_ACCESS_KEY_ID = None  # ./local_env.py
AWS_SECRET_ACCESS_KEY = None  # ./local_env.py
AWS_SES_AUTO_THROTTLE = False
