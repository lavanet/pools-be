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
