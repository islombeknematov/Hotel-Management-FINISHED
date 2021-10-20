from django.urls import path

from homePage.views import ContactCreateView, ContactDeleteView, ContactUpdateView

app_name = 'contact'

urlpatterns = [
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='delete'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='update'),
    path('', ContactCreateView.as_view(), name='create_contact'),
]
