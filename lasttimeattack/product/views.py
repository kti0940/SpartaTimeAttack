from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import (
    Product as ProductModel,
    Subscribe as SubscribeModel
)

# Create your views here.

class ProductView(APIView):
    def get(self, request):
        product = ProductModel.objects.all()
        return Response(ProductSerializer(product).data, many=True)