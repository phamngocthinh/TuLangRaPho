from django.db import models

from home.models import BaseModel, ProductType


class ProductTypeTranslate(BaseModel):
    lang_code = models.CharField(db_column='lang_code', max_length=10, blank=True, null=False)
    type_id = models.ForeignKey(to=ProductType, on_delete=models.CASCADE, db_column='type_id', blank=False,
                                null=False)
    type_name = models.CharField(db_column='type_name', max_length=100, blank=True, null=False)
    description = models.CharField(db_column='description', max_length=200, blank=True, null=False)

    class Meta:
        db_table = 'product_type_translates'
