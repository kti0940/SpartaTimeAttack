from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
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
        
        article = ArticleSerializer(ArticleModel.objects.filter(startdate__lte=timezone.now(), enddate__gte=timezone.now()), many=True).data
        print(article)
        
        return Response(article)
        
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
    
        title = request.data.get('title')
        content = request.data.get('content')
        category = request.data.get('category')
        
        user = UserModel.objects.get(username = request.user.username)
        # print(f'오브젝트 겟 ->{user}')
        
        if len(title) < 5:
            return Response({"message":"제목은 5자 이상이어야 합니다."})
        elif len(content) < 20:
            return Response({"message":"콘텐츠는 20자 이상이어야 합니다"})
        elif category == '' or None:
            return Response({"message":"카테고리를 선택해 주세요"})
        
        category = Category.objects.get(name=request.data.get('category'))
        article = ArticleModel(
            title=title, 
            content=content, 
            user=user
            )
        article.save()
        article.category.add(category)
        
        return Response({"message":"게시글이 작성 되었습니다"})
    
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
