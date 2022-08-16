from django.db import models
from user.models import User

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "product"

    product_name = models.CharField(max_length=256)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_img = models.CharField(max_length=256)
    product_description = models.CharField(max_length=256)
    product_price = models.CharField(max_length=256)
    product_stock = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Category(models.Model):
    class Meta:
        db_table = "categories"

    category = models.CharField(max_length=256)

class OrderStatus(models.Model):
    class Meta:
        db_table = "order_status"

    author = models.ForeignKey('User', on_delete=models.CASCADE)
    order_complete = models.CharField(max_length=256)
    complete_payment = models.CharField(max_length=256)
    start_delivery = models.CharField(max_length=256)
    delivery_completed = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class ProductOrder(models.Model):
    class Meta:
        db_table = "product_order"

    author = models.ForeignKey('User', on_delete=models.CASCADE)
    order_count = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)