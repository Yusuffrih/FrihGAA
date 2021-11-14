from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products.as_view(), name='products')
]
