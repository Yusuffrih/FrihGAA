from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq, name='faq'),
    path('add/', views.add_faq, name='add_faq'),
]
