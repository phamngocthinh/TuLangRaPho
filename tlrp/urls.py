from django.urls import path

from tlrp import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]