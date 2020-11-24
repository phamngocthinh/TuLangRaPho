from django.db import models

from home.models import BaseModel, Product


class Blog(BaseModel):
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, db_column='product_id', null=False)
    image_path = models.CharField(db_column='image_path', max_length=100, null=False)

    class Meta:
        db_table = 'blogs'
