from django.db import models


class NetworkType(models.TextChoices):
    MAINNET = 'mainnet', 'Mainnet'
    TESTNET = 'testnet', 'Testnet'


class RewardType(models.TextChoices):
    MANUAL = 'manual', 'Manual'
    ONCHAIN = 'onchain', 'Onchain'
