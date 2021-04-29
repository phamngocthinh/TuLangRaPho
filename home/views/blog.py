from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from home.models import Blog, BlogTranslate
from django.db import connection


class BlogView(TemplateView):
    template_name = 'blog/index.html'

    def get_header(seft, request):
        return render(request, seft.template_name)

    def get_context_data(self, **kwargs):
        blogs = Blog.objects.all()
        blog_translates = BlogTranslate.objects.all()
        # blog_translates = BlogTranslate.objects.filter(blog_id=blogs.values('id'))
        context = {
            'blog_translates': blog_translates.filter(lang_code='vn')
        }
        return context