from django.contrib import admin

from libs.admin_register import AdminRegister
from . import models


@AdminRegister(models.Chain)
class ChainAdmin(admin.ModelAdmin):
    pass


@AdminRegister(models.Reward)
class RewardAdmin(admin.ModelAdmin):
    pass
