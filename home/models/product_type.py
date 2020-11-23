from django.db import models

from home.models import BaseModel


class ProductType(BaseModel):
    # product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, db_column='product_id', null=False)

    class Meta:
        db_table = 'product_types'
