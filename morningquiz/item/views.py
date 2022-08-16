from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from item.models import Item as ItemModel

# Create your views here.

class ItemView(APIView):
    def get(self,request):
        
        return Response(CategorySerializer(request.user))