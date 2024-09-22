from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


def username_field(**kwargs):
    default_kwargs = {
        'verbose_name': _('username'),
        'max_length': 30,
        'unique': True,
        'help_text': _('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        'validators': [
            validators.RegexValidator(
                code='invalid',
                regex=r'^[\w.@+-]+$',
                message=_('Enter a valid username. This value may contain only letters, '
                          'numbers and @/./+/-/_ characters.'),
            ),
        ],
        'error_messages': {'unique': _("A user with that username already exists."),},
    }
    default_kwargs.update(kwargs)
    return models.CharField(**default_kwargs)
