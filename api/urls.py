from django.urls import path

from api.views import RoomModelListAPIView
app_name = 'api'

urlpatterns = [
    path('room/', RoomModelListAPIView.as_view(), name='room_api')
]