import re
from decimal import Decimal

from django.core.files import File
from django.db import models
from django.db.models import Q
from django.utils.timezone import now

from apps.core.coingecko.classes import CoinGeckoQuery
from apps.core.kvstore.models import KeyValue
from apps.core.lava_queries.classes import LavaQuery, LavaQueryException
from libs.utils import logger, download_file
from .constants import NetworkType, RewardType
from .utils import get_month, get_days_left, can_update_coingecko


class Chain(models.Model):
    chain_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    rpc_node_runners = models.PositiveIntegerField(default=0)
    denom = models.ForeignKey('Denom', on_delete=models.PROTECT, related_name='chains', null=True, blank=True)
    past_rewards = models.DecimalField(max_digits=36, decimal_places=12, default=0)
    future_rewards = models.DecimalField(max_digits=36, decimal_places=12, default=0)
    past_rewards_usd = models.DecimalField(max_digits=36, decimal_places=2, default=0)
    future_rewards_usd = models.DecimalField(max_digits=36, decimal_places=2, default=0)
    current_rewards = models.DecimalField(max_digits=36, decimal_places=12, default=0)
    rewards_end_month = models.CharField(max_length=16, null=True, blank=True)
    total_requests = models.PositiveBigIntegerField(default=0)
    logo = models.ImageField(upload_to='chain-logos/', null=True, blank=True)
    coingecko_id = models.CharField(max_length=64, null=True, blank=True)
    coingecko_last_update = models.DateTimeField(null=True, blank=True)
    rpc_url = models.URLField(null=True, blank=True)
    estimated_apr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.chain_id

    re_clean_name = re.compile(r'main ?net', re.IGNORECASE)

    @property
    def clean_name(self):
        return self.re_clean_name.sub('', self.name).strip().capitalize()

    def _sum_rewards(self, rewards):
        rewards = rewards.select_related('denom').order_by('month')
        monthly_rewards = {
            reward.month: (reward.get_amount(), reward.get_amount_usd())
            for reward in rewards
            if reward.reward_type == RewardType.ONCHAIN}
        # Manual rewards override on-chain rewards for the same month.
        for reward in rewards:
            if reward.reward_type == RewardType.MANUAL:
                monthly_rewards[reward.month] = (reward.get_amount(), reward.get_amount_usd())

        total_token = Decimal(0)
        total_usd = Decimal(0)
        for token, usd in monthly_rewards.values():
            total_token += token or 0
            total_usd += usd or 0
        return total_token, total_usd

    def update_past_rewards(self, current_month):
        self.past_rewards, self.past_rewards_usd = self._sum_rewards(
            self.rewards.filter(month__lt=current_month))

    def update_future_rewards(self, current_month):
        self.future_rewards, self.future_rewards_usd = self._sum_rewards(
            self.rewards.filter(Q(month__gte=current_month) | Q(month=None)))

    def update_current_rewards(self, current_month):
        self.current_rewards = Decimal(0)
        if current := self.rewards.filter(month=current_month).order_by('reward_type').first():
            self.current_rewards = current.get_amount()

    def update_rewards(self, current_month=None, commit=True):
        current_month = current_month or KeyValue.get(f'mainnet_current_month')
        self.update_past_rewards(current_month)
        self.update_future_rewards(current_month)
        self.update_current_rewards(current_month)
        if commit:
            self.save(update_fields=[
                'past_rewards',
                'future_rewards',
                'past_rewards_usd',
                'future_rewards_usd',
                'current_rewards',
            ])

    def update_rewards_end_month(self, current_month):
        self.rewards_end_month = None
        if latest_reward := self.rewards.order_by('month').last():
            if latest_reward.month is None:
                self.rewards_end_month = 'TBD'
            elif latest_reward.month >= current_month:
                self.rewards_end_month = str(latest_reward.month)
            else:
                self.rewards_end_month = None

    @property
    def total_rewards(self):
        return self.past_rewards + self.future_rewards

    @property
    def total_rewards_usd(self):
        return self.past_rewards_usd + self.future_rewards_usd

    def update_chain_rpc_providers(self):
        self.rpc_node_runners = 0
        for network in NetworkType:
            lavaquery = LavaQuery(network=network)
            try:
                result = lavaquery.query_providers(self.chain_id)
                self.rpc_node_runners += len(result.stakeEntry)
            except LavaQueryException:
                pass
        logger.debug('update_chain_rpc_providers(): %s, rpc_node_runners: %s',
                     self.chain_id, self.rpc_node_runners)
        self.save(update_fields=['rpc_node_runners'])

    def update_total_requests(self):
        self.total_requests = self.block_requests.aggregate(
            total_requests=models.Sum('requests'))['total_requests'] or 0
        self.save(update_fields=['total_requests'])

    def update_coingecko_price(self, commit=True, force=False):
        if can_update_coingecko(self, force=force):
            logger.debug('update_coingecko_price(): %s, cgid: %s', self, self.coingecko_id)
            coin = CoinGeckoQuery.query_coin(coin_id=self.coingecko_id)
            if not self.denom:
                self.denom, created = Denom.objects.update_or_create(
                    denom=coin['symbol'],
                    defaults={
                        'coingecko_id': self.coingecko_id,
                        'coingecko_last_update': now(),
                        'price': coin['market_data']['current_price']['usd'],
                    }, )
            if not self.logo:
                self.logo = File(download_file(coin['image']['large']), name=f'{self.chain_id}.png')
            self.coingecko_last_update = now()
            if commit:
                self.save(update_fields=['denom', 'logo', 'coingecko_last_update'])


class Denom(models.Model):
    denom = models.CharField(max_length=32, primary_key=True)
    ibc_denom = models.CharField(max_length=68, null=True, blank=True)
    price = models.DecimalField(verbose_name='Price (USD)', max_digits=36, decimal_places=12, default=0)
    coingecko_id = models.CharField(max_length=64, null=True, blank=True)
    coingecko_last_update = models.DateTimeField(null=True, blank=True)
    microtoken_factor = models.PositiveBigIntegerField(default=1, blank=True)

    def __str__(self):
        return self.denom or self.ibc_denom

    @classmethod
    def create_from_ibc(cls, ibc_denom, network=NetworkType.MAINNET):
        if ibc_denom.startswith('ibc/'):
            lavaquery = LavaQuery(network=network)
            result = lavaquery.query_denom_trace(ibc_denom.split('/')[-1])
            base_denom = result.denom_trace.base_denom
        else:
            base_denom = ibc_denom
        self = cls.objects.create(
            denom=base_denom,
            ibc_denom=ibc_denom,)
        return self

    def get_amount(self, amount):
        return Decimal(amount) / Decimal(self.microtoken_factor or 1)

    def to_usd(self, amount, usd_price=None):
        return Decimal(self.get_amount(amount) * (usd_price or self.price)).quantize(Decimal('1'))

    def update_coingecko_price(self, commit=True, force=False):
        if can_update_coingecko(self, force=force):
            logger.debug('update_coingecko_price(): %s, cgid: %s', self, self.coingecko_id)
            coin = CoinGeckoQuery.query_coin(coin_id=self.coingecko_id)
            self.price = coin['market_data']['current_price']['usd']
            self.coingecko_last_update = now()
            if commit:
                self.save(update_fields=['denom', 'coingecko_last_update'])


class MicroDenom(models.Model):
    denom = models.CharField(max_length=32, primary_key=True)
    ibc_denom = models.CharField(max_length=68, null=True, blank=True)


class Reward(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE, related_name='rewards')
    denom = models.ForeignKey(Denom, on_delete=models.PROTECT, related_name='rewards', null=True, blank=True)
    month = models.PositiveIntegerField(null=True, blank=True,
                                        help_text='Blank (empty) value is a future reward shown as "TBD".')
    reward_amount = models.DecimalField(max_digits=36, decimal_places=12, default=0)
    reward_type = models.CharField(max_length=16, choices=RewardType.choices, default=RewardType.MANUAL,
                                   help_text='Manual rewards will be counted instead of OnChain reward '
                                             'for the same month if both exist.', )
    price_usd = models.DecimalField(max_digits=16, decimal_places=4, null=True, blank=True)

    class Meta:
        unique_together = ('chain', 'denom', 'month', 'reward_type',),

    def __str__(self):
        return f'{self.chain.chain_id} - {self.month or 'TBD'}'

    def get_amount(self):
        return self.denom.get_amount(self.reward_amount)

    def get_amount_usd(self):
        if self.price_usd:
            return self.denom.to_usd(self.reward_amount, usd_price=self.price_usd)
        if self.denom and self.denom.coingecko_id:
            return self.denom.to_usd(self.reward_amount)


class BlockRequest(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE, related_name='block_requests')
    network = models.CharField(max_length=12, choices=NetworkType.choices, default=NetworkType.MAINNET)
    height = models.PositiveBigIntegerField()
    requests = models.PositiveIntegerField()

    class Meta:
        unique_together = ('chain', 'height', 'network', ),

    def __str__(self):
        return f'{self.chain_id} - {self.height}'
