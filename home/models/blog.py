from django.db import models

from home.models import BaseModel, Product


class Blog(BaseModel):
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, db_column='product_id', null=False)
    content = models.TextField(db_column='content', null=True)

    class Meta:
        db_table = 'product_types'
