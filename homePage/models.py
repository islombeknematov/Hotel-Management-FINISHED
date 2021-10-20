
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactModel(models.Model):

    name = models.CharField(max_length=32, verbose_name=_('name'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('email'), null=True, blank=True)
    message = models.TextField(verbose_name=_('message'), null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')














