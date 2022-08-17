from email import contentmanager
from tabnanny import verbose
from django.db import models
from user.models import User as UserModel
from datetime import datetime
from django.utils import timezone

# Create your models here.

#  카테고리 이름, 설명이 들어간 모델 생성
class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
#글 작성자, 글 제목, 카테고리, 글 내용 (카테고리 두개이상 선택해야함)
    # 외래 키를 활용하여 작성자와 카테고리의 관계를 맺어야함
class Article(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    contents = models.TextField()
    exposure_start_date = models.DateField("게시 시작 일자", default=timezone.now)
    exposure_end_date = models.DateField("게시 종료 일자", default=timezone.now)
    datetime = models.DateTimeField(auto_now_add=True) # 데이트타임 필드 = timezone.now() #데이트필드 = time.now()
    def __str__(self):
        return f'({self.title}) 라는 제목으로 {self.user.username} 님이 작성하신 글입니다'
    
class Comment(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    contents = models.TextField("본문")
    
    def __str__(self):
        return f'{self.article.title} / {self.contents}'
    
    
    