from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import F

from django.contrib.auth import login, logout, authenticate

from user.models import UserProfile

from user.serializers import UserSerializer

# Create your views here.

class UserView(APIView):
    # permission_classes = [permissions.AllowAny] # 모든 사용자 사용 가능
    permission_classes = [permissions.IsAuthenticated] # 인증된 사용자만 사용 가능
    # permission_classes = [permissions.IsAdminUser] #어드민 유저만 사용 가능

    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)
        
        # hobbys = user.userprofile.hobby.all()
        
        # # print(hobbys)
        # for hobby in hobbys:
        #     # exclde : 매칭 된 쿼리만 제외, filter와 반대
        #     # annotate : 필드 이름을 변경해주기 위해 사용, 이외에도 원하는 필드를 추가하는 등 다양하게 활용 가능
        #     # values / values_list : 지정한 필드만 리턴 할 수 있음. values는 dict로 return, values_list는 tuple로 ruturn
        #     # F() : 객체에 해당되는 쿼리를 생성함
            
        #     hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
        #     print(hobby_members)
        #     hobby_members = list(hobby_members)
        #     print(f"hobby : {hobby.name} / hobby members : {hobby_members}")
        # return Response({})
        
        # print(dir(user))
        
        # 역참조를 사용 했을 때
        # one-to-one filed 는 예외로 _set이 붙지 않는다.
        # hobbys = user.userprofile.hobby.all()
        
        # print(hobbys)
        
        # 역참조를 사용하지 않았을 때
        # user_profile = UserProfile.objects.get(user=user)
        # hobbys = user_profile.hobby.all()
        # print(hobbys)
        
    
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