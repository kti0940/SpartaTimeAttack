from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/<str:name>', views.dinner, name='dinner'),
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
]
