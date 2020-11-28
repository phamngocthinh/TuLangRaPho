from django.db import models

from home.models import BaseModel, Role


class User(BaseModel):
    name = models.CharField(db_column='name', max_length=100, blank=True, null=True)
    role_id = models.ForeignKey(to=Role, on_delete=models.CASCADE, db_column='role_id')
    user_name = models.CharField(db_column='user_name', max_length=50, blank=True, null=True)
    password = models.CharField(db_column='password', max_length=50, blank=True, null=True)
    enable = models.IntegerField(db_column='enable', blank=True, null=True, default=1)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.user_name
