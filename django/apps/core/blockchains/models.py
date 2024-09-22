import re
from decimal import Decimal

from django.db import models

from apps.core.kvstore.models import KeyValue


class Chain(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=128)
    rpc_node_runners = models.PositiveIntegerField(default=0)
    denom = models.CharField(max_length=32)
    denom_price = models.DecimalField(max_digits=32, decimal_places=18, default=0)
    past_rewards = models.DecimalField(max_digits=32, decimal_places=18, default=0)
    future_rewards = models.DecimalField(max_digits=32, decimal_places=18, default=0)
    logo = models.ImageField(upload_to='chain_logos/', null=True, blank=True)

    def __str__(self):
        return self.clean_name()

    re_clean_name = re.compile(r'main ?net', re.IGNORECASE)

    def clean_name(self):
        return self.re_clean_name.sub('', self.name).strip().capitalize()

    def _sum_rewards(self, lookup, current_month=None):
        lookup = {f'month__{lookup}': current_month or KeyValue.get('current_month')}
        amount = self.reward_set.filter(**lookup).aggregate(amount=models.Sum('reward_amount'))['amount']
        return amount or Decimal(0)

    def update_past_rewards(self, current_month=None):
        self.past_rewards = self._sum_rewards('lt', current_month=current_month)

    def update_future_rewards(self, current_month=None):
        self.future_rewards = self._sum_rewards('gte', current_month=current_month)


class RewardType(models.TextChoices):
    MANUAL = 'Manual'
    ONCHAIN = 'OnChain'


class Reward(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    height = models.PositiveBigIntegerField(null=True, blank=True)
    month = models.PositiveIntegerField()
    reward_amount = models.PositiveIntegerField()
    reward_type = models.CharField(max_length=16, choices=RewardType.choices)

    def __str__(self):
        return f'{self.chain.name} - {self.month}'


class Denom(models.Model):
    ibc_denom = models.CharField(max_length=64, primary_key=True)
    denom = models.CharField(max_length=32)

    def __str__(self):
        return self.denom
