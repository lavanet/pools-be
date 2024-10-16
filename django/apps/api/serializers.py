from rest_framework import serializers

from apps.core.blockchains import models
from apps.core.blockchains.utils import get_days_left, get_month


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chain
        fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reward
        fields = '__all__'


class ChainCardSerializer(serializers.ModelSerializer):
    rewards_end = serializers.SerializerMethodField()
    rewards_days_remaining = serializers.SerializerMethodField()

    class Meta:
        model = models.Chain
        fields = [
            'id',
            'chain_id',
            'name',
            'clean_name',
            'denom',
            'logo',
            'past_rewards',
            'future_rewards',
            'current_rewards',
            'total_rewards',
            'past_rewards_usd',
            'future_rewards_usd',
            'total_rewards_usd',
            'rpc_node_runners',
            'total_requests',
            'rewards_end_month',
            'estimated_apr',
            'rpc_url',
            'rewards_end',
            'rewards_days_remaining',
        ]

    def get_name(self, instance):
        return instance.clean_name()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['service'] = 'RPC'
        return data

    def get_rewards_end(self, instance):
        try:
            return get_month(int(instance.rewards_end_month) + 1).strftime('%b %d, %Y')
        except:
            return instance.rewards_end_month  # TBD / null

    def get_rewards_days_remaining(self, instance):
        try:
            return get_days_left(int(instance.rewards_end_month) + 1).days
        except:
            pass
