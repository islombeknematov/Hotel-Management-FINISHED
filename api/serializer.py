from rest_framework import serializers

from rooms.models import RoomModel


class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        exclude = ('title_en', 'title_ru', 'title_uz')


