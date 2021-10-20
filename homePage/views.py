from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView
from homePage.forms import ContactModelForm
from homePage.models import ContactModel


class ContactCreateView(CreateView):
    template_name = 'navbar/contact.html'
    form_class = ContactModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactModel.objects.all().order_by('-pk')
        return context

    def get_success_url(self):
        return reverse('contact:create_contact')


class ContactUpdateView(UpdateView):
    template_name = 'cntcEditForm.html'
    form_class = ContactModelForm
    success_url = '/contact/'
    model = ContactModel


class ContactDeleteView(DeleteView):
    model = ContactModel
    success_url = '/contact/'


class BannerTemplateView(TemplateView):
    template_name = 'navbar/mainPage.html'




