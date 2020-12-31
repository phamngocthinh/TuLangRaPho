from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import CategoryTranslate, Category, ProductTranslate, ProductTypeTranslate


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        categories = CategoryTranslate.objects.all()
        products = ProductTranslate.objects.all().filter(lang_code='vn').select_related('product_id')
        product_types = ProductTypeTranslate.objects.all()
        context = {
            'categories': categories.filter(lang_code='vn'),
            'products': products,
            'product_types': product_types.filter(lang_code='vn'),
            'special_products': products.order_by('product_id__rank')[:10]
        }
        return context
