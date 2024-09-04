from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class UserManager(DjangoUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_active=True,
            date_joined=now(),
            **extra_fields
        )
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, **fields):
        return self._create_user(is_staff=False, is_superuser=False, **fields)

    def create_superuser(self, **fields):
        return self._create_user(is_staff=True, is_superuser=True, **fields)

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username.lower()})


class LCaseEmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return value.lower() if value else value


class AuthUser(AbstractBaseUser, PermissionsMixin, models.Model):
    """
    Based class of all users in proprio direct. Names, email and language code added.
    Used for the admin
    """
    email = LCaseEmailField(_('Email'), unique=True)
    date_joined = models.DateTimeField(_('date joined'), default=now)
    is_staff = models.BooleanField(
        _('Staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. '
                    'Unselect this instead of deleting accounts.'),
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True

    def __str__(self):
        return self.email

    get_short_name = __str__
    get_full_name = __str__
