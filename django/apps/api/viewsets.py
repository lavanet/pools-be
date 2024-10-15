from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response

from apps.api.serializers import ChainSerializer, RewardSerializer, ChainCardSerializer
from apps.core.blockchains.models import Chain, Reward
from apps.core.kvstore.models import KeyValue


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


class HomeViewSet(viewsets.ViewSet):
    def list(self, request):
        totals = KeyValue.fetch(['total_rewards', 'total_past_rewards', 'total_future_rewards', 'total_requests'])
        chains = ChainCardSerializer(Chain.objects.filter(is_active=True), many=True)
        return Response({
            'chains': chains.data,
            **totals,
        })
