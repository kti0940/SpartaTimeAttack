from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user
    
    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CommentModel
        fields = ["contents"]
        
class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source="comment_set")
    
    def get_category(self, obj):
        return [category.name for category in obj.category.all()]
    
    class Meta:
        model = ArticleModel
        fields = ["user","category", "title","contents", "comments"]
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ["instrodution", "birthday", "age"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    articles = ArticleSerializer(many=True, source="article_set")
    comments = CommentSerializer(many=True, source='comment_set')
    
    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date" ,"userprofile", "articles", "comments"]
        