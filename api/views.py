from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from api.serializer import RoomModelSerializer
from rooms.models import RoomModel


class RoomModelListAPIView(ListAPIView):
    queryset = RoomModel.objects.all()
    serializer_class = RoomModelSerializer


