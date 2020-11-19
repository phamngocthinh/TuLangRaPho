from django.db import models


class ProductType(models.Model):
    id = models.SmallAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=25, blank=True, null=True)
    description = models.TextField(db_column='description', blank=True, null=True)
    create_time = models.DateTimeField(db_column='create_time', blank=True, null=True)
    update_time = models.DateTimeField(db_column='update_time', blank=True, null=True)
    create_user = models.IntegerField(db_column='create_user', blank=True, null=True)
    update_user = models.IntegerField(db_column='update_user', blank=True, null=True)
    delete_flag = models.IntegerField(db_column='delete_flag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_types'
