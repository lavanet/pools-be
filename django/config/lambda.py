# https://github.com/adamchainz/apig-wsgi
from apig_wsgi import make_lambda_handler

from .wsgi import application

handler = make_lambda_handler(application)
