from .settings import *  # noqa

DEBUG = False

TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.app_directories.Loader',
    )),
)
