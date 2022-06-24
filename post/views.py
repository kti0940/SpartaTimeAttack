from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q
from post.serializers import CompanySerializer
from post.serializers import JobPostSerializer
from post.serializers import JobPostSkillSetModelSerializer

class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = int( request.data.get("job_type", None) )
        company_name = request.data.get("company_name", None)

        return Response(status=status.HTTP_200_OK)

class CompanyView(APIView):
    
    def get(self, request):
        # company = Company.objects.all()
        # print(company)
        print(CompanySerializer(many=True).data)
        return Response({})
    