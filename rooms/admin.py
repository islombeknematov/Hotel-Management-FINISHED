from django.contrib import admin

# Register your models here.
from modeltranslation.admin import TranslationAdmin

from rooms.models import RoomModel, BookInfoModel


@admin.register(RoomModel)
class RoomModelAdmin(TranslationAdmin):
    list_display = ['title', 'price']
    search_fields = ['title']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BookInfoModel)
class BookInfoModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone',
                    # 'arrival', 'departure'
                    ]
    search_fields = ['first_name']
    list_filter = ['created_at']

