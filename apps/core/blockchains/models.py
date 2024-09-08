import re

from django.db import models


class Chain(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=128)
    reward_month = models.PositiveBigIntegerField(default=0)
    month_remaining = models.PositiveIntegerField(default=0)
    rpc_node_runners = models.PositiveIntegerField(default=0)
    denom = models.CharField(max_length=32)
    denom_price = models.DecimalField(max_digits=32, decimal_places=18, default=0)
    past_rewards = models.DecimalField(max_digits=32, decimal_places=18, default=0)
    logo = models.ImageField(upload_to='chain_logos/', null=True, blank=True)

    def __str__(self):
        return self.clean_name()

    re_clean_name = re.compile(r'main ?net', re.IGNORECASE)

    def clean_name(self):
        return self.re_clean_name.sub('', self.name).strip().capitalize()


class RewardType(models.TextChoices):
    MANUAL = 'Manual'
    ONCHAIN = 'OnChain'


class Reward(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    height = models.PositiveBigIntegerField()
    month = models.PositiveIntegerField()
    reward_amount = models.PositiveIntegerField()
    reward_type = models.CharField(max_length=16, choices=RewardType.choices)

    def __str__(self):
        return f'{self.chain.name} - {self.height}'
