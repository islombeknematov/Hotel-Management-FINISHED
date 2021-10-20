from django.db import models
from django.utils.translation import gettext as _

from embed_video.fields import EmbedVideoField


class AboutModel(models.Model):
    video = EmbedVideoField(verbose_name=_('video'))   # same like models.URLField()
    description = models.CharField(max_length=128, null=True, verbose_name=_('description'))

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('about')
        verbose_name_plural = _('about')




