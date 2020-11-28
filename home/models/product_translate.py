from django.db import models

from home.models import BaseModel, Product


class ProductTranslate(BaseModel):
    lang_code = models.CharField(db_column='lang_code', max_length=10, blank=False, null=False, default="")
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, db_column='product_id', blank=False,
                                   null=False, default=None)
    product_name = models.CharField(db_column='product_name', max_length=100, blank=True, null=False)
    description = models.CharField(db_column='description', max_length=200, blank=True, null=False)

    class Meta:
        db_table = 'product_translates'
