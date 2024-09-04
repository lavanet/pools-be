from django.conf import settings
from django.template import Library
from django.utils.translation import get_language

from ..registry import templates
from ..utils import prepend_domain

register = Library()
register.filter(name='full_url')(prepend_domain)


@register.inclusion_tag('emails/header.html')
def header():
    return {
        'templates': templates.values(),
    }


@register.inclusion_tag('emails/language_selector.html')
def language_selector():
    return {
        'languages': settings.LANGUAGES,
        'current_language': get_language(),
    }
