from django.db import models

from home.models import BaseModel, Category, ProductType


class Product(BaseModel):
    product_type_id = models.ForeignKey(to=ProductType, on_delete=models.CASCADE, db_column='product_type_id',
                                        blank=True, null=True)
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE, db_column='category_id')
    image_path = models.CharField(db_column='image_path', max_length=150, blank=True, null=False)

    class Meta:
        db_table = 'products'
