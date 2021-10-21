from django.contrib.auth import get_user_model
from django.db import models, IntegrityError

# from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _
# Create your models here.


UserModel = get_user_model()


class RoomModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('title'))
    image = models.ImageField(upload_to='covers', verbose_name=_('image'))
    price = models.CharField(max_length=32, verbose_name=_('price'))

    kitchen = models.ImageField(upload_to='covers', verbose_name=_('kitchen'), null=True, blank=True)
    living = models.ImageField(upload_to='covers', verbose_name=_('living room'), null=True, blank=True)
    bathroom = models.ImageField(upload_to='covers', verbose_name=_('bathroom'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('room')
        verbose_name_plural = _('rooms')


class WishlistModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name=_('wishlist'))
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name=_('wishlist'))

    def __str__(self):
        return self.room.title


    @staticmethod
    def add_or_remove(user, room):
        try:
            WishlistModel.objects.create(user=user, room=room)
        except IntegrityError:
            WishlistModel.objects.get(user=user, room=room).delete()


    class Meta:
        verbose_name = _('wishlist')
        verbose_name_plural = _('wishlist')
        unique_together = 'user', 'room'


class BookListModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name=_('book_room'))
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name=_('book_room'))

    def __str__(self):
        return self.room.title

    @staticmethod
    def book_update(user, room):
        try:
            BookListModel.objects.create(user=user, room=room)
        except IntegrityError:
            BookListModel.objects.get(user=user, room=room).delete()

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('book')
        unique_together = 'user', 'room'




class BookInfoModel(models.Model):

    # bookRoom = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='bookRoom')

    arrival = models.DateField(max_length=20, verbose_name=_('arrival'), blank=True, null=True)
    departure = models.DateField(max_length=20, verbose_name=_('departure'), blank=True, null=True)

    first_name = models.CharField(max_length=20, verbose_name=_('first_name'), null=True, blank=True)
    last_name = models.CharField(max_length=20, verbose_name=_('last_name'), null=True, blank=True)
    email = models.CharField(max_length=32, verbose_name=_('email'), null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name=_('phone'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.first_name or ''

    class Meta:
        verbose_name = _('bookinfo')
        verbose_name_plural = _('bookinfos')

