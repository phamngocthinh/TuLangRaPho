from django.db import models


class Role(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=100, blank=True, null=True)
    enable = models.IntegerField(db_column='enable', blank=True, null=True, default=1)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.name
