import re
import unicodedata
from _socket import getdefaulttimeout, setdefaulttimeout, gethostbyaddr
from threading import currentThread

from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.functional import cached_property

from .loggers import logger
from .settings import PROJECT_DOMAIN_URL

__author__ = 'snake'
_request = {}

re_email_loose = re.compile(r'.+@.+\..+')
re_email = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$')
re_sequential_signs = re.compile(r'\W{2,}')
re_http = re.compile(r'^https?://')


def clean_template_name(template):
    """
    Support template names with or without
    the .html extension.
    """
    if not template.endswith('.html'):
        template += '.html'
    return template


def prod_cached_property(func):
    """
    Wraps with property in debug and
    cached_property in prod.
    """
    return property(func) if settings.DEBUG else cached_property(func)


def clean_recipients(recipients):
    """
    Clean email addresses before sending to
    minize human errors.
    """
    return (strip_accents(recipient).strip() for recipient in recipients)


def valid_email_or_none(email):
    """
    Clean an email address. Return None if
    it's still invalid after the clean.
    """
    try:
        email = strip_accents(email.strip().lower())
        if re_email.match(email) and not re_sequential_signs.search(email):
            return email
    except (AttributeError, ValueError, TypeError):
        pass


def prepend_domain(url):
    """
    Transform absolute url into a full url
    with domain if it doesn't have one.
    """
    if not re_http.match(url):
        url = PROJECT_DOMAIN_URL + url
    return url


def strip_accents(s):
    """
    Remove diacritics from a string.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def get_request(hostname=False):
    try:
        request = _request[currentThread()]
    except KeyError:
        request = None
    else:
        if not hasattr(request, 'remote_ip'):
            request.remote_ip = request.META.get('X-Real-IP', request.META.get('REMOTE_ADDR'))
        if hostname and not hasattr(request, 'hostname'):
            request.hostname = get_hostname(request.remote_ip)
    return request


def set_request(request):
    _request[currentThread()] = request


def get_hostname(ip, timeout=1):
    oldtimeout = getdefaulttimeout()
    try:
        setdefaulttimeout(timeout)
        hostname = gethostbyaddr(ip)[0]
    except:
        logger.warning('Could not resolve ip [%s]' % ip)
    else:
        return hostname
    finally:
        setdefaulttimeout(oldtimeout)


def test_email(to, subject='Email Test', message='This is a test message. Everything is fine.',
               from_email=settings.DEFAULT_FROM_EMAIL):
    email = EmailMessage(to=to, subject=subject, body=message, from_email=from_email)
    email.attach(filename='test.txt', content='This is a file. ' * 10000, mimetype='text/plain')
    email.attach(filename='test2.txt', content='This is a file2. ' * 10000, mimetype='text/plain')
    email.send()
