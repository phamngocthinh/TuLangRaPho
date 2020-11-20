from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'blog/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)