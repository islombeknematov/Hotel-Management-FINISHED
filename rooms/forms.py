from django import forms

from rooms.models import BookInfoModel


class BookInfoModelForm(forms.ModelForm):
    class Meta:
        model = BookInfoModel
        exclude = ['created_at']
