from __future__ import absolute_import, unicode_literals

from os import environ, path

from celery import Celery
from django.conf import settings

PROJECT_NAME = path.basename(path.dirname(__file__))
environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery(PROJECT_NAME)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


def periodic_task(*args, run_every, **kwargs):
    def _decorator(func):
        task = app.task(func, *args, **kwargs)
        app.add_periodic_task(
            schedule=run_every,
            sig=task.s(), )
        return task

    return _decorator
