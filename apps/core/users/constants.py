from libs.auth_user.trans import i18n_auth_user

authentification_set = (i18n_auth_user('Authentification'), {'fields': (
    'email',
    'password',
)})

personal_info_set = (i18n_auth_user('Personal info'), {'fields': (
    'first_name',
    'last_name',
)})

options_set = (i18n_auth_user('Options'), {'fields': (
    'lang',
    'can_receive_emails',
)})

admin_set = (i18n_auth_user('Admin'), {'fields': (
    'is_active',
    'is_staff',
    'is_superuser',
    'last_login',
    'date_joined',
)})

ALL_FIELDSETS = (authentification_set, personal_info_set, options_set, admin_set)
ALL_AUTHOR_FIELDSETS = (authentification_set, personal_info_set, options_set,
                        admin_set)
