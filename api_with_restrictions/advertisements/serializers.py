from django.contrib.auth.models import User
from rest_framework import serializers
from django.forms import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    def validate(self, data):
        if data.__len__() == 1:
            return super().validate(data)
        count = {}
        for ad in Advertisement.objects.all():
            if ad.creator in count and ad.status == 'OPEN':
                count[ad.creator].append(ad.id)
            elif ad.creator not in count and ad.status == 'OPEN':
                count[ad.creator] = [ad.id]
        for el, val in count.items():
            if val.__len__() >= 10:
                raise ValidationError("User couldn't have more than 10 adv.!")
        return data
