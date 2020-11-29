from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import CategoryTranslate, Category, ProductTranslate, Product


class CategoryView(TemplateView):
    template_name = 'home/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        categories = CategoryTranslate.objects.all()
        products = Product.objects.all()
        context = {
            'categories': categories.filter(lang_code='vn'),
            'products': products.filter(id=kwargs['id'])
        }
        return context
