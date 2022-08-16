from django.contrib import admin
from django.urls import path, include
from .views import SkillView, JobView, CompanyView

urlpatterns = [
    path('', SkillView.as_view()),
    path('job', JobView.as_view()),
    path('company', CompanyView.as_view()),
]
