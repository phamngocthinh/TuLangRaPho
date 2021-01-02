from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import ProductTypeTranslate, Category, ProductTranslate, Product, CategoryTranslate


class TypeView(TemplateView):
    template_name = 'type/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        # get type info with **kwargs
        types = ProductTypeTranslate.objects.all().filter(lang_code='vn', type_id=kwargs.get('id'))
        # get all product of type
        products = Product.objects.all().filter(product_type_id=kwargs.get('id'))
        # get all product of types by language
        products_translate = ProductTranslate.objects.all().filter(lang_code='vn',product_id__in=products)
        # get all product categories
        categories = CategoryTranslate.objects.all().filter(lang_code='vn')
        # get all product special
        special_products_translate = ProductTranslate.objects.all().filter(lang_code='vn').select_related('product_id')
        context = {
            'type': types[0],
            'products': products_translate,
            'categories': categories,
            'special_products': special_products_translate.order_by('product_id__rank')[:5]
        }
        return context
