from django.urls import path
from . import views

urlpatterns = [
    path('', views.Memberships.as_view(), name='memberships')
]
