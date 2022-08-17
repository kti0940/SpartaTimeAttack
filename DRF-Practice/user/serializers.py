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
    comments = CommentSerializer(many=True, source="comment_set", read_only=True)
    
    def get_category(self, obj):
        return [category.name for category in obj.category.all()]
    
    class Meta:
        model = ArticleModel
        fields = ["user", "category", "title","contents", "comments"]
        

class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()    # 없는 필드를 만들어서 가져오고 싶을때, 변수를 선언하고 get_변수명 을 쓴 함수를 정의함
    def get_same_hobby_users(self, obj):
        # obj : hobby model의 object가 나오고, name이 나오게 model을 만들어서 이름이 찍힘
        # print(type(obj))
        # print(obj)
        
        # dir(obj) 프린트해보면 userprofile_set이 있음! 역참조를 해서 전부 가져오게 함  
        # hobby를 역참조하고 있는 userprofile 의 user의 username을 가져옴
        
        user_list =[]
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)
        return user_list
        
        # list 축약식 쓰면 이렇게 한줄로 가져올 수 있음 / all 대신 본인 이름 빼려면 exclude쓰면 됨
        # return [user_profile.user.username for user_profile in obj.userprofile_set.all()]
    
    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]  # fields에는 있는 필드만 들어가야 함
        
        # 위의 내용처럼 실행할 필요 없이(SerializerMethodField()사용할 필요 없이) 바로 역참조로 가져 올 수도 있음
        # fields = ["name", "userprofile_set"]
        
class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True, read_only=True)
    get_hobbys = serializers.ListField(required=False)
    
    class Meta:
        model = UserProfileModel
        fields = ["instrodution", "birthday", "age", "hobby", "get_hobbys"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    articles = ArticleSerializer(many=True, source="article_set", read_only=True)
    # comments = CommentSerializer(many=True, source='comment_set')
    
    # validate : 기존 validation + custom validation
    def validate(self, data):
        if not data.get("email", "").endswith("@naver.com"):
            raise serializers.ValidationError(
                detail={"error":"네이버 이메일만 가입 할 수 있습니다"}
            )
        return data
            
    # 기존 함수를 덮어씀 (create는 인자로 validated_data가 들어감)
    def create(self, validated_data):
        user_profile = validated_data.pop("userprofile")
        user = UserModel(**validated_data)
        get_hobbys = user_profile.pop("get_hobbys",[])
        print(user_profile)
        print(f'겟 하비 -> {get_hobbys}')
        
        user.save()
        
        user_profile = UserProfileModel.objects.create(
                user=user, 
                **user_profile
            )
        user_profile.hobby.add(*get_hobbys)
        return user
        

    class Meta:
        model = UserModel
        fields = ["username", "password", "email", "fullname", "join_date",
                    "userprofile", "articles"]
        
        extra_kwargs = {
            # write_only : 해당 필드를 쓰기 전용으로 만들어 준다.
            # 쓰기 전용으로 설정 된 필드는 직렬화 된 데이터에서 보여지지 않는다.
            'password': {'write_only': True}, # default : False
            'email': {
                # error_messages : 에러 메세지를 자유롭게 설정 할 수 있다.
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.'
                    },
                    # required : validator에서 해당 값의 필요 여부를 판단한다.
                    'required': False # default : True
                    },
            }