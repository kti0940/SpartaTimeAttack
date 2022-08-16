from django.db import models
from user.models import User as UserModel

# Create your models here.
class Product(models.Model):
    product_name = models.CharField("상품명", max_length=100)
    description = models.TextField("설명")
    price = models.IntegerField("가격")
    introduction_date = models.DateTimeField()
    active = models.BooleanField("활성화여부")
    
    def __str__(self):
        return f"이 상품은 {self.product_name} 입니다"
    

class Subscribe(models.Model):
    user = models.ForeignKey(UserModel, verbose_name=("유저"), on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", verbose_name=("상품명"), on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    subscription_startdate = models.DateTimeField()
    subscription_enddate = models.DateTimeField()
    
    def __str__(self):
        return f"{self.product}"