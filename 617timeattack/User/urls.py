from django.contrib import admin
from django.urls import path, include
from User import views

urlpatterns = [
    path('', views.UserView.as_view()),
]