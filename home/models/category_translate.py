from django.db import models

from home.models import BaseModel, Category


class ProductTranslate(BaseModel):
    lang_code = models.CharField(db_column='lang_code', max_length=10, blank=False, null=False)
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE, db_column='category_id', blank=False,
                                    null=False)
    category_name = models.CharField(db_column='category_name', max_length=100, blank=True, null=False)
    description = models.CharField(db_column='description', max_length=200, blank=True, null=False)

    class Meta:
        db_table = 'product_translates'
