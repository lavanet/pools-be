from django.contrib import admin

from libs.admin_register import AdminRegister
from . import models


@AdminRegister(models.KeyValue)
class KeyValueAdmin(admin.ModelAdmin):
    pass
