from django.db import models


class Category(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=250, blank=True, null=False)

    class Meta:
        db_table = 'categories'