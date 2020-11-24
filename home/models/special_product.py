from django.db import models

from home.models import BaseModel, ProductType


class Product(BaseModel):
    product_id = models.ForeignKey(to=ProductType, on_delete=models.CASCADE, db_column='product_id', blank=True,
                                   null=True)
    index = models.IntegerField(db_column='index', blank=True, null=False)

    class Meta:
        db_table = 'products'
