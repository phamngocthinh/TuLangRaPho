from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home.views import home, blog, about, contact, category

urlpatterns = [
    path('', home.HomeView.as_view(), name='home'),
    path(r'category/<int:id>', category.CategoryView.as_view(), name='category'),
    path(r'blogs/', blog.BlogView.as_view(), name='blog'),
    path(r'about/', about.AboutView.as_view(), name='about'),
    path(r'contact/', contact.ContactView.as_view(), name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
