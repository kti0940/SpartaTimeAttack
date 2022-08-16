from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.
class UserView(APIView):
    def get(self, request):
        return Response({'massage': 'get method!!'})
    
    def post(self, request):
        return Response({'massage': 'post method!!'})
