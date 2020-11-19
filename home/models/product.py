from django.db import models


class Product(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    product_type = models.IntegerField(db_column='product_type', blank=True, null=True)
    category = models.IntegerField(db_column='category', blank=True, null=True)
    create_time = models.DateTimeField(db_column='create_time', blank=True, null=True)
    update_time = models.DateTimeField(db_column='update_time', blank=True, null=True)
    create_user = models.IntegerField(db_column='create_user', blank=True, null=True)
    update_user = models.IntegerField(db_column='update_user', blank=True, null=True)
    delete_flag = models.IntegerField(db_column='delete_flag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
