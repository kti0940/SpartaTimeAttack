from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='product_view'),
]
