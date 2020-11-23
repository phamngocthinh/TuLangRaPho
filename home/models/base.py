from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    create_time = models.DateTimeField(db_column='create_time', blank=True, null=True)
    update_time = models.DateTimeField(db_column='update_time', blank=True, null=True)
    create_user = models.IntegerField(db_column='create_user', blank=True, null=True)
    update_user = models.IntegerField(db_column='update_user', blank=True, null=True)
    delete_flag = models.IntegerField(db_column='delete_flag', blank=True, null=False, default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)
