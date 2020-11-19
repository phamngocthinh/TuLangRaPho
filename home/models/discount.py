from django.db import models

from home.models import Product


class Discount(models.Model):
    id = models.SmallAutoField(db_column='id', primary_key=True)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, db_column='product_id')
    discount = models.FloatField(db_column='discount', blank=True, null=True)
    effected_start_date = models.DateTimeField(db_column='effected_start_date', blank=True, null=True)
    effected_end_date = models.DateTimeField(db_column='effected_end_date', blank=True, null=True)
    activation = models.IntegerField(db_column='activation', blank=True, null=True)
    create_time = models.DateTimeField(db_column='create_time', blank=True, null=True)
    update_time = models.DateTimeField(db_column='update_time', blank=True, null=True)
    create_user = models.IntegerField(db_column='create_user', blank=True, null=True)
    update_user = models.IntegerField(db_column='update_user', blank=True, null=True)
    delete_flag = models.IntegerField(db_column='delete_flag', blank=True, null=True)

    class Meta:
        db_table = 'discount'

    def __str__(self):
        return self.discount
