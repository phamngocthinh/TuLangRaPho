from django.db import models

from home.models import BaseModel
class Category(BaseModel):
    class Meta:
        db_table = 'categories'