from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ["title"]
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ["contents"]
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ["instrodution", "birthday", "age"]


class UserSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    userprofile = UserProfileSerializer()
    
    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date" ,"userprofile", "article_set", "comment_set"]
        