from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from about.models import AboutModel


# CLASS BASED VIEW

# class AboutTemplateView(TemplateView):
#     template_name = 'about.html'


    # FUNCTION BASED VIEW
def about_video(request):
    my_video = AboutModel.objects.all()
    context = {
        'my_video': my_video
    }
    return render(request, 'navbar/about.html', context)



