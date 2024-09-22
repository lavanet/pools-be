from django.conf import settings

__author__ = 'snake'

USER_EMAIL_FIELD = getattr(settings, 'EMAIL_USER_EMAIL_FIELD', 'email')
USER_LANG_FIELD = getattr(settings, 'EMAIL_USER_LANG_FIELD', 'lang')
USER_ACTIVE_FIELD = getattr(settings, 'EMAIL_USER_ACTIVE_FIELD', 'can_receive_emails')

PROJECT_DOMAIN_URL = getattr(settings, 'PROJECT_DOMAIN', '')

USE_CELERY = getattr(settings, 'EMAIL_USE_CELERY', not settings.DEBUG)
CELERY_QUEUE = getattr(settings, 'EMAIL_CELERY_QUEUE', '')
MAX_RETRIES = getattr(settings, 'EMAIL_MAX_RETRIES', 2)
RETRY_DELAY = getattr(settings, 'EMAIL_RETRY_DELAY', 30)
RATE_LIMIT = getattr(settings, 'EMAIL_RATE_LIMIT', 25)
