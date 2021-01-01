from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import Product, ProductTranslate, Category, CategoryTranslate


class ProductDetailView(TemplateView):
    template_name = 'product_detail/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        product = Product.objects.all()
        product_translates = ProductTranslate.objects.filter(product_id=kwargs.get('id'), lang_code='vn', product_id__in=product.values('id'))
        category = CategoryTranslate.objects.filter(category_id=product_translates[0].product_id.category_id, lang_code='vn')[0]
        context = {
            'product_detail': product_translates,
            'category': category
        }
        return context
