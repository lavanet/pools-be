from django.contrib import admin, messages

from libs.admin_register import AdminRegister
from . import models
from ..coingecko.classes import CoinGeckoException


@AdminRegister(models.Chain)
class ChainAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.coingecko_id:
            try:
                obj.update_coingecko_price(commit=False)
            except CoinGeckoException:
                self.message_user(request, f'ID {obj.coingecko_id} not found in Coingecko', level=messages.ERROR)
        obj.save()


@AdminRegister(models.Reward)
class RewardAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        obj.chain.update_rewards()


@AdminRegister(models.Denom)
class DenomAdmin(admin.ModelAdmin):
    pass


@AdminRegister(models.BlockRequest)
class BlockRequestAdmin(admin.ModelAdmin):
    pass
