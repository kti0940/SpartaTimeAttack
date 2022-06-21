from django.db import models
from user.models import User as UserModel
from datetime import datetime

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField(upload_to='uploads/', null=True)
    description = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now_add=True)
    startdate = models.DateTimeField("게시 시작 시간", default=datetime.now)
    enddate = models.DateTimeField("게시 종료 시간", default=datetime.now)
