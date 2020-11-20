from django.urls import path

from home.views import home
from home.views import blog

urlpatterns = [
    path('', home.HomeView.as_view(), name='home'),
    path('blogs/', blog.BlogView.as_view(), name='blog'),
]
