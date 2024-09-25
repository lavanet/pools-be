# https://github.com/adamchainz/apig-wsgi

from apig_wsgi import make_lambda_handler

from .lambda_management import management_handler
from .wsgi import application

django_handler = make_lambda_handler(application)


def handler(event, context):
    if event.get('manage'):
        return management_handler(event, context)
    return django_handler(event, context)
