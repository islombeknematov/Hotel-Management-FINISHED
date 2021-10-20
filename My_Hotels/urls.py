from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('social/', include('allauth.urls'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),


    # path('book/', include('book.urls', namespace='book')),
    path('', include('homePage.urls', namespace='homePage')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('about/', include('about.urls', namespace='about')),
    path('room/', include('rooms.urls', namespace='room')),
    path('api/', include('api.urls', namespace='api')),


    path('accounts/', include('registration.backends.default.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
