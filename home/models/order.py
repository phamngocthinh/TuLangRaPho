from django.db import models

from home.models import BaseModel, Product


class Order(BaseModel):
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, db_column='product_id', related_name='order')
    customer_id = models.IntegerField(db_column='customer_id', blank=True, null=True)
    order_date = models.DateTimeField(db_column='order_date', blank=True, null=False)
    order_status = models.IntegerField(db_column='order_status', blank=False, null=False, default=1)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.order
