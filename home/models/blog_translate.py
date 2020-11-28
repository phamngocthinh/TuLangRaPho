from django.db import models

from home.models import BaseModel, Blog


class BlogTranslate(BaseModel):
    blog_id = models.ForeignKey(to=Blog, on_delete=models.CASCADE, db_column='blog_id', blank=False, null=False)
    lang_code = models.CharField(db_column='lang_code', max_length=10, blank=False, null=False)
    title = models.CharField(db_column='title', max_length=100, blank=False, null=False)
    content = models.TextField(db_column='content', blank=True, null=False)

    class Meta:
        db_table = 'blog_translates'
