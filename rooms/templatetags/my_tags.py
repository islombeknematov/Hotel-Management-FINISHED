from django.template import Library

from rooms.models import WishlistModel, BookListModel

register = Library()


@register.filter
def liked_room(my_room, user):
    return WishlistModel.objects.filter(user=user, room=my_room).exists()


@register.filter
def book_room(my_room, user):
    return BookListModel.objects.filter(user=user, room=my_room).exists()
