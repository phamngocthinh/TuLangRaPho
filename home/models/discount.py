from django.db import models

from home.models import BaseModel, Product


class Discount(BaseModel):
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, db_column='product_id', related_name='discount')
    discount = models.FloatField(db_column='discount', blank=True, null=True)
    effected_start_date = models.DateTimeField(db_column='effected_start_date', blank=False, null=False)
    effected_end_date = models.DateTimeField(db_column='effected_end_date', blank=False, null=False)
    activation = models.IntegerField(db_column='activation', blank=False, null=False, default=1)

    class Meta:
        db_table = 'discount'

    def __str__(self):
        return self.discount
