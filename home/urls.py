from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from home.views import home, blog, about, contact, category, product_detail, type, cart

urlpatterns = [
    path('', home.HomeView.as_view(), name='home'),
    path(r'category/<int:id>', category.CategoryView.as_view(), name='category'),
    path(r'type/<int:id>', type.TypeView.as_view(), name='type'),
    path(r'blogs/', blog.BlogView.as_view(), name='blog'),
    path(r'about/', about.AboutView.as_view(), name='about'),
    path(r'contact/', contact.ContactView.as_view(), name='contact'),
    path(r'product_detail/<int:id>', product_detail.ProductDetailView.as_view(), name='product_detail'),
    path(r'cart/', cart.CartView.as_view(), name='cart'),
    # ajax api
    path(r'check_product_exist/', home.check_product_exist, name="check_product_exist"),
    path(r'check_list_product_exist/', home.check_list_product_exist, name="check_list_product_exist"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
