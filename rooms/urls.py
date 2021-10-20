from django.conf.urls.i18n import i18n_patterns
from django.urls import path

from rooms.views import edit_wishlist, WishListView, RoomListView, BookListView, update_book, room_detail, \
    BookInfoCreateView, cancel_book

app_name = 'room'

urlpatterns = [
    path('<int:pk>/wishlist/', edit_wishlist, name='edit-wishlist'),
    path('<int:pk>/update_book/', update_book, name='update-book'),

    path('wishlist/', WishListView.as_view(), name='heart-wishlist'),
    path('book/', BookListView.as_view(), name='book'),

    path('<int:pk>/', room_detail, name='room-detail'),

    path('bookinfo/', BookInfoCreateView.as_view(), name='bookinfo'),
    path('bookinfo/<int:pk>/cancel/', cancel_book, name='cancel'),

    path('', RoomListView.as_view(), name='my_room'),
]



