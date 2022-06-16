from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate

# Create your views here.

class UserView(APIView):
    # permission_classes = [permissions.AllowAny] # 모든 사용자 사용 가능
    permission_classes = [permissions.IsAuthenticated] # 인증된 사용자만 사용 가능
    # permission_classes = [permissions.IsAdminUser] #어드민 유저만 사용 가능
    
    # 사용자 정보 조회
    def get(self, request):
        return Response({"message": "get method!!"})
    
    # 회원 가입
    def post(self, request):
        return Response({"message": "post method!!"})
    
    # 회원 정보 수정
    def put(self, request):
        return Response({"message": "put method!!"})
    
    # 회원 탈퇴
    def delete(self, request):
        return Response({"message": "delete method!!"})
    
class UserAPIView(APIView):
    # permission_classes = [permissions.AllowAny]
    
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        
        print(user)
        
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다"})
        
        
        login(request, user)   
        
        return Response({"message": "login success!!"})

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"massage": "logout success!!"})