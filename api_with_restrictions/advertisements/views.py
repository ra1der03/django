from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (ModelViewSet)
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer
from rest_framework.filters import SearchFilter
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = AdvertisementFilter
    filterset_fields = ['status', ]
    search_fields = ['creator__id', 'title', 'status', ]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
