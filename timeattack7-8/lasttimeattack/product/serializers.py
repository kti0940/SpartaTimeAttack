from rest_framework import serializers

from .models import (
    Product as ProductModel,
    Subscribe as SubscribeModel
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'