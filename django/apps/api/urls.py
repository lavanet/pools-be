from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.viewsets import ChainViewSet, RewardViewSet, HomeViewSet

router = DefaultRouter()
router.register('home', HomeViewSet, basename='home')
router.register('chains', ChainViewSet)
router.register('rewards', RewardViewSet)

urlpatterns = [
    path('auth/', include('apps.api.api_auth.urls')),
    path('', include('apps.api.yasg_urls')),
    path('', include(router.urls)),
]
