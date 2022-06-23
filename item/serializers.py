from rest_framework import serializers

from item.models import Category as CategoryModel
from item.models import Item as ItemModel
from item.models import Order as OrderModel
from item.models import ItemOrder as ItemOrderModel

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ["name", "category", "image_url"]

class CategorySerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    
    class Meta:
        model = CategoryModel
        fields = ["name", "name", "category", "image_url"]