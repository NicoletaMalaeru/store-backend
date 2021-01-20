from . import views
from django.urls import path, include
from rest_auth.views import LoginView


urlpatterns = [
    path('products_list', views.products_list, name = 'products_list'),
]
