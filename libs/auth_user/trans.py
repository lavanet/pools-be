from django.utils.translation import gettext_lazy as _

trans = {
    'user': _('user'),
    'users': _('users'),
    'first name': _('first name'),
    'last name': _('last name'),
    'The two password fields didn\'t match.': _('The two password fields didn\'t match.'),
    'Password': _('Password'),
    'Password confirmation': _('Password confirmation'),
    'Enter the same password as before, for verification.': _('Enter the same password as before, for verification.'),
    'Authentification': _('Authentification'),
    'Personal info': _('Personal info'),
    'Options': _('Options'),
    'Admin': _('Admin'),
}


def i18n_auth_user(text):
    try:
        return trans[text]
    except KeyError:
        raise ValueError('Translation not found "%s".' % text)
