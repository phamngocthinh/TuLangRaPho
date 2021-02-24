# coding=utf-8
from rest_framework import serializers

from home.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  # 'product_type_id',
                  # 'category_id',
                  # 'image_path',
                  # 'rank',
                  # 'price',
                  # 'create_time',
                  # 'update_time',
                  # 'create_user',
                  # 'update_user',
                  'delete_flag'
                  )
