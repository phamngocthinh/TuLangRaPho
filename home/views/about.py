from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)
