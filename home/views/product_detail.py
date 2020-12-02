from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import Product, ProductTranslate


class ProductDetailView(TemplateView):
    template_name = 'product_detail/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        # product_detail = Product.objects.all()
        product_translates = ProductTranslate.objects.filter(product_id=kwargs.get('id'))
        context = {
            'product_detail': product_translates.filter(lang_code='vn')
        }
        return context
