from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import CategoryTranslate


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        categories = CategoryTranslate.objects.all()
        context = {
            'categories': categories
        }
        return context
