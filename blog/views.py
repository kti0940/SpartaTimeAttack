from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from user.models import User as UserModel
from blog.models import Article as ArticleModel, Category
from blog.models import Comment as CommentModel
from user.serializers import ArticleSerializer
# from DRF.permissions import RegistedMoreThanAMinuteUser
from datetime import datetime
from django.utils import timezone
from DRF.permissions import IsAdminOrIsAuthenticatedReadOnly



class ArticleView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
    # 로그인 한 사용자의 게시글 목록 return
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [RegistedMoreThanAMinuteUser]

    def get(self, request):
        # user = request.user
        # print(user)
        
        #-----
        # 민기님 코드
        # articles = ArticleModel.objects.filter(exposure_start_date__lte=datetime.now(), exposure_end_date__gte=datetime.now()).order_by('-datetime')
        # serializer = ArticleSerializer(articles, many=True)
        
        # return Response(serializer.data)
        #------
        user = request.user
        today = timezone.now() # 현재 시각을 정의해줌
        articles = ArticleModel.objects.filter(
            exposure_start_date__lte=today,
            exposure_end_date__gte=today,
        ).order_by("-id") # 아이디값으로 역순정렬
        # article = ArticleSerializer(ArticleModel.objects.filter(startdate__lte=timezone.now(), enddate__gte=timezone.now()), many=True).data
        serializer = ArticleSerializer(articles, many=True).data
        
        return Response(serializer, status=status.HTTP_200_OK)
        
        # articles = ArticleModel.objects.filter(user=user)
        # print(f'아티클스는 -> {articles}')
        # print(f'아티클스는 데이터타임은 {articles}')
        
        # titles = [article.title for article in articles] # list 축약 문법

        # titles = []

        # for article in articles:
        #     titles.append(article.title)
        
        # return Response({"article_list": titles})
        
        # article_data = ArticleSerializer(ArticleModel.objects.filter(user=request.user), many=True).data
        # print(article_data)
        
        
    def post(self, request):
        user = request.user
        request.data['user'] = user.id
        article_serializer = ArticleSerializer(data = request.data)
        
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(article_serializer.data, status=status.HTTP_200_OK)
        
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # request.data['user'] = user.id
        # article_serializer = ArticleSerializer(data = request.data)
        # print(f'article -> {article_serializer}')
        
        # if article_serializer.is_valid():
        #     article_serializer.save()
        #     return Response(article_serializer.data, status=status.HTTP_200_OK)
        
        # return Response(article_serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        # user = request.user
        
        # title = request.data.get('title', "")
        # print(f'타이틀은 {title}')
        # contents = request.data.get('contents', "")
        # print(f'콘텐츠는 -> {contents}')
        # categorys = request.data.pop('category', [])
        # print(f'카테고리는 -> {categorys}')
        
        # user = UserModel.objects.get(username = request.user.username)
        # print(f'오브젝트 겟 ->{user}')
        
        # if len(title) <= 5:
        #     return Response({"message":"제목은 5자 이상이어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)
        # if len(contents) <= 20:
        #     return Response({"message":"콘텐츠는 20자 이상이어야 합니다"}, status=status.HTTP_400_BAD_REQUEST)
        # if not categorys:
        #     return Response({"message":"카테고리를 선택해 주세요"}, status=status.HTTP_400_BAD_REQUEST)
        
        # article = ArticleModel(
        #     user = user,
        #     **request.data
        #     )
        # article.save()
        # article.category.add(*categorys)
        # category = request.data.pop('category')
        
        return Response({"message":"게시글이 작성 되었습니다"}, status=status.HTTP_200_OK)
    
class CommentView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        print(user)
        
        comments = CommentModel.objects.filter(user=user)
        print(f'코멘트는 -> {comments}')
        
        contents = []
        
        for comment in comments:
            contents.append(comment.contents)
            
        print(contents)

        return Response({"comment_list": contents})
