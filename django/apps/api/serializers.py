from rest_framework import serializers

from apps.core.blockchains import models


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chain
        fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reward
        fields = '__all__'


class ChainCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chain
        fields = [
            'id',
            'chain_id',
            'name',
            'clean_name',
            'denom',
            'logo',
            'future_rewards',
            'total_rewards',
            'total_rewards_usd',
            'past_rewards',
            'rpc_node_runners',
            'total_requests',
            'months_remaining',
            'rewards_per_month',
            'estimated_apr',
        ]

    def get_name(self, instance):
        return instance.clean_name()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['months_remaining'] = instance.months_remaining or 'TBD'
        data['service'] = 'RPC'
        return data
