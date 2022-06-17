from email import contentmanager
from tabnanny import verbose
from django.db import models
from user.models import User

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
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    datetime = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.title} {self.user.username} 님이 작성하신 글입니다'
    
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    contents = models.TextField("본문")
    def __str__(self):
        return f'{self.contents}'
    
    