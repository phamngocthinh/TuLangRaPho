from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)
