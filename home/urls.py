from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home.views import home, blog, about, contact

urlpatterns = [
    path('', home.HomeView.as_view(), name='home'),
    path('blogs/', blog.BlogView.as_view(), name='blog'),
    path('about/', about.AboutView.as_view(), name='about'),
    path('contact/', contact.ContactView.as_view(), name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
