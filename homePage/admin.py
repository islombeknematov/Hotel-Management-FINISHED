from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from homePage.models import ContactModel


# Register your models here.

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    # list_display_links = ['created_at']
    list_display = ['name', 'email', 'phone']
    list_filter = ['created_at']
    search_fields = ['name']

    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }


