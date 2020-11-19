from django.db import models

from home.models.role import Role


class User(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=100, blank=True, null=True)
    role_id = models.ForeignKey(to=Role, on_delete=models.CASCADE, db_column='role_id', blank=True)
    user_name = models.CharField(db_column='user_name', max_length=50, blank=True, null=True)
    password = models.CharField(db_column='password', max_length=100, blank=True, null=True)
    enable = models.IntegerField(db_column='enable', blank=True, null=True)
    create_time = models.DateTimeField(db_column='create_time', blank=True, null=True)
    update_time = models.DateTimeField(db_column='update_time', blank=True, null=True)
    create_user = models.IntegerField(db_column='create_user', blank=True, null=True)
    update_user = models.IntegerField(db_column='update_user', blank=True, null=True)
    delete_flag = models.IntegerField(db_column='delete_flag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
