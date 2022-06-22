from django.db import models
from user.models import User as UserModel
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    description = models.TextField("설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    exposure_start_date = models.DateField("노출 시작 일자")
    exposure_end_date = models.DateField("노출 종료 일자")
    
    def __str__(self):
        return self.title
