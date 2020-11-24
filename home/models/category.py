from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'categories'
