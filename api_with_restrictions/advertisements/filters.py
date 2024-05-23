from django_filters import rest_framework as filters
from django.conf import settings
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    creator = filters.CharFilter(field_name='creator')
    created_at = filters.DateTimeFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Advertisement
        fields = ['created_at', ]



