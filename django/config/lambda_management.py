# https://github.com/adamchainz/apig-wsgi
from os import environ

from django.core.management import call_command


def management_handler(event, context):
    management_event = event.get('manage')
    if management_event == 'migrate':
        call_command('migrate')
    elif management_event == 'collectstatic':
        call_command('collectstatic', '--noinput')
    elif management_event == 'createsuperuser':
        environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.{environ.get('SETTINGS', 'settings')}')
        from apps.core.users.models import User
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                email=event.get('email'),
                password=event.get('password'))
    elif management_event == 'blockchains':
        call_command('blockchains', event.get('arg'))
    return {'message': 'Management command executed', }
