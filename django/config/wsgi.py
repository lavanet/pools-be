"""
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from os import environ

from django.core.wsgi import get_wsgi_application

environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.{environ.get('SETTINGS', 'settings')}')
application = get_wsgi_application()
