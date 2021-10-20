from django.contrib import admin

# Register your models here.
from embed_video.admin import AdminVideoMixin

from about.models import AboutModel


# @admin.register(AboutVideoModel)
class AboutModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['video', 'description']
admin.site.register(AboutModel, AboutModelAdmin)



