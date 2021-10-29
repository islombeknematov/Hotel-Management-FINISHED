from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from django.views.generic import ListView, DetailView, CreateView, DeleteView

from rooms.forms import BookInfoModelForm
from rooms.models import RoomModel, WishlistModel, BookListModel, BookInfoModel


class RoomListView(LoginRequiredMixin, ListView):
    template_name = 'navbar/room.html'
    paginate_by = 6

    def get_queryset(self):
        qs = RoomModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = RoomModel.objects.filter(title__icontains=q)

        return qs


class WishListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'

    def get_queryset(self):
        return RoomModel.objects.filter(wishlist__user=self.request.user)


@login_required
def edit_wishlist(request, pk):
    room = get_object_or_404(RoomModel, pk=pk)
    WishlistModel.add_or_remove(request.user, room)

    return redirect(request.GET.get('next', '/'))


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'navbar/book.html'

    def get_queryset(self):
        return RoomModel.objects.filter(book_room__user=self.request.user)


@login_required
def update_book(request, pk):
    room = get_object_or_404(RoomModel, pk=pk)
    BookListModel.book_update(request.user, room)

    return redirect(request.GET.get('next', '/'))


def room_detail(request, pk):
    # ------------------------------
    # try:
    #     detail_room = RoomModel.objects.get(pk=pk)
    # except RoomModel.DoesNotExist:
    #     raise Http404      #   |
    #                          SAME
    #                       #   |
    room = get_object_or_404(RoomModel, pk=pk)
    # ----------------------------------------
    context = {
        'detail': room
    }
    return render(request, 'room_detail.html', context)


class BookInfoCreateView(CreateView):
    template_name = 'navbar/book.html'
    form_class = BookInfoModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookinfo_temp'] = BookInfoModel.objects.all().order_by('-pk')
        return context

    def get_success_url(self):
        return reverse('room:bookinfo')



def cancel_book(request, pk):
    cancel = get_object_or_404(BookInfoModel, pk=pk)
    cancel.delete()
    return redirect('/room/bookinfo')
