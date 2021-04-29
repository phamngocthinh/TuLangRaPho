from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class CartView(TemplateView):
    template_name = 'cart/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)
