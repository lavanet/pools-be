from django.contrib.auth.admin import UserAdmin as DjUserAdmin

from libs.admin_register import AdminRegister
from . import models, constants


@AdminRegister(models.User)
class UserAdmin(DjUserAdmin):
    fieldsets = constants.ALL_FIELDSETS
    list_display = 'id', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login',
    readonly_fields = 'last_login', 'date_joined',
    filter_horizontal = 'groups', 'user_permissions',
    ordering = '-pk',
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
