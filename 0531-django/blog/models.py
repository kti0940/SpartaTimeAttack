from pydoc import describe
from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "Category"
        
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=256, unique=True)

class Article(models.Model):
    class Meta:
        db_table = "my_article"
        
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.CharField(max_length=256)