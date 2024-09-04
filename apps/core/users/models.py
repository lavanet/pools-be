from django.db import models

from libs.auth_user.models import AuthUser
from libs.auth_user.trans import i18n_auth_user
from libs.emails.mixins import EmailMixin


class User(EmailMixin, AuthUser):
    user_type = 'user'

    class Meta:
        verbose_name = i18n_auth_user('user')
        verbose_name_plural = i18n_auth_user('users')

    first_name = models.CharField(i18n_auth_user('first name'), max_length=128, default='', blank=True)
    last_name = models.CharField(i18n_auth_user('last name'), max_length=128, default='', blank=True)

    def get_full_name(self):
        return ' '.join((self.first_name, self.last_name))

    get_short_name = get_full_name
