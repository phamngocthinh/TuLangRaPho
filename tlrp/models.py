from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_type = models.IntegerField(db_column='PRODUCT_TYPE', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user = models.IntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    update_user = models.IntegerField(db_column='UPDATE_USER', blank=True, null=True)  # Field name made lowercase.
    delete_flag = models.IntegerField(db_column='DELETE_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCT'

class ProductTranslate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_type = models.IntegerField(db_column='PRODUCT_TYPE', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user = models.IntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    update_user = models.IntegerField(db_column='UPDATE_USER', blank=True, null=True)  # Field name made lowercase.
    delete_flag = models.IntegerField(db_column='DELETE_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCT_TRANSLATE'

class ProductType(models.Model):
    id = models.SmallAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user = models.IntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    update_user = models.IntegerField(db_column='UPDATE_USER', blank=True, null=True)  # Field name made lowercase.
    delete_flag = models.IntegerField(db_column='DELETE_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCT_TYPE'

class Discount(models.Model):
    id = models.SmallAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    discount = models.FloatField(db_column='DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    effected_start_date = models.DateTimeField(db_column='EFFECTED_START_DATE', blank=True, null=True)  # Field name made lowercase.
    effected_end_date = models.DateTimeField(db_column='EFFECTED_END_DATE', blank=True, null=True)  # Field name made lowercase.
    activation = models.IntegerField(db_column='ACTIVATION', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user = models.IntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    update_user = models.IntegerField(db_column='UPDATE_USER', blank=True, null=True)  # Field name made lowercase.
    delete_flag = models.IntegerField(db_column='DELETE_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DISCOUNT'

class User(models.Model):
    id = models.SmallAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_role_id = models.SmallIntegerField(db_column='USER_ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user = models.IntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    update_user = models.IntegerField(db_column='UPDATE_USER', blank=True, null=True)  # Field name made lowercase.
    delete_flag = models.IntegerField(db_column='DELETE_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER'
