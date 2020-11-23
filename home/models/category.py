from django.db import models

from home.models import BaseModel


class Category(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)
    category_name = models.CharField(db_column='category_name', max_length=250, blank=True, null=False)
    description = models.CharField(db_column='description', max_length=200, blank=True, null=False)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category_name
