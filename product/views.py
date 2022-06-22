from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from product.serializers import ProductSerializer

# Create your views here.
class ProductView(APIView):
    
    def post(self,request):
        # return Response({"message":"post"})
        request.data['user'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        return Response({"message":"put"})