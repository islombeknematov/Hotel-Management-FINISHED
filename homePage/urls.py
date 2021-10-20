from django.urls import path, include

from homePage.views import BannerTemplateView

app_name = 'homePage'


urlpatterns = [
    path('', BannerTemplateView.as_view(), name='banner'),
]