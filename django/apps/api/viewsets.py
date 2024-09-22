from rest_framework import viewsets, permissions, filters

from apps.api.serializers import ChainSerializer, RewardSerializer
from apps.core.blockchains.models import Chain, Reward


class ChainViewSet(viewsets.ModelViewSet):
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']


class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
