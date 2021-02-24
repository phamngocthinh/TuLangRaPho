from http import HTTPStatus
from django.core.serializers.json import DjangoJSONEncoder

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from requests import Response
from rest_framework import serializers
from rest_framework.utils import json

from home.models import CategoryTranslate, Category, ProductTranslate, ProductTypeTranslate, Product
from home.serializers import ProductSerializer


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
            'special_products': products.order_by('product_id__rank')[:5]
        }
        return context

@csrf_exempt
def postFriend(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get data from request
        product_id = request.POST['product_id']
        data = {
            'is_taken': Product.objects.filter(id=product_id)
            # 'is_taken': Product.objects.filter(id=product_id).exists()
        }

        # response = HttpResponse(data)
        # response.content
        # return HttpResponse(data)
        courses = Product.objects.filter(id=product_id).first()
        serializer = ProductSerializer(data=courses)
        if serializer.is_valid(True):
            return Response(serializer.data, status=200)
        print(serializer.errors)

        # return response
        # check exist product
        # if Product.objects.filter(id=product_id).exists():
        #     return JsonResponse("ThinhPN",status=HTTPStatus.OK)
        # else:
        #     return JsonResponse(status=HTTPStatus.NOT_FOUND)
    # some error occured
    return JsonResponse(status=HTTPStatus.INTERNAL_SERVER_ERROR)
