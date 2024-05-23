from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (ModelViewSet)
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from rest_framework.filters import SearchFilter
from rest_framework.throttling import AnonRateThrottle

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = [AdvertisementFilter, ]
    search_fields = ['creator__id', 'title', ]
    permission_classes = ['IsOwnerOrReadOnly', ]
    throttle_classes = [AnonRateThrottle, ]


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

