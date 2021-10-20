from django.urls import path

from about.views import about_video

app_name = 'about'

urlpatterns = [
    path('', about_video, name='video'),
]
