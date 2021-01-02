from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import CategoryTranslate, Category, ProductTranslate, Product, ProductTypeTranslate


class CategoryView(TemplateView):
    template_name = 'category/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        # get category info with **kwargs
        categories = CategoryTranslate.objects.all().filter(lang_code='vn', category_id=kwargs.get('id'))
        # get all product of categories
        products = Product.objects.all().filter(category_id=kwargs.get('id'))
        # get all product of categories by language
        products_translate = ProductTranslate.objects.all().filter(lang_code='vn',product_id__in=products)
        # get all product types
        product_types = ProductTypeTranslate.objects.all()
        # get all product special
        special_products_translate = ProductTranslate.objects.all().filter(lang_code='vn').select_related('product_id')
        context = {
            'category': categories[0],
            'products': products_translate,
            'product_types': product_types.filter(lang_code='vn'),
            'special_products': special_products_translate.order_by('product_id__rank')[:5]
        }
        return context
