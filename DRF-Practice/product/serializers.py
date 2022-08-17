from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfile
from user.models import Hobby as Hobby

from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel
from blog.models import Category as CategoryModel

from product.models import Product as ProductModel

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    
    class Meta:
        model = ProductModel
        fields = ["user", "title", "thumbnail", "description", 
                    "created", "exposure_start_date", "exposure_end_date",]
        
        

        