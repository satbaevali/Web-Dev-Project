from rest_framework import serializers
from .models import User, SwapRequest, Skill, SkillCategory, LearningRequest,TeachingOffer
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email', 'password','first_name','last_name','bio','profile_picture','date_joined','last_login',]
        read_only_fields = ['date_joined', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True}
        } #extra_kwargs = {'password': {'write_only': True}} — чтобы пароль не отображался в ответе API, но можно было его отправить при регистрации.
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class SkillCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ['id','name','description']

class  SkillSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=SkillCategory.objects.all(),
        source='category', # Указывает, что это поле связано с полем 'category' модели
        write_only=True,   # Поле используется только для записи (не будет в JSON ответе)
        allow_null=True,   # Разрешаем не указывать категорию
        required=False     # Делаем поле необязательным
    )

    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'category', 'category_id']

class TeachingOfferSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    skill =  SkillSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),source = 'user',write_only = True  
    )
    skill_id = serializers.PrimaryKeyRelatedField(
        queryset = Skill.objects.all(),source = 'skill',write_only = True
    )
    

    class Meta:
        model = TeachingOffer
        fields = ['id','user', 'skill', 'description','experience_level','status','created_at','updated_at', 'user_id','skill_id',]
        read_only_fields = ('created_at', 'updated_at')

class LearningRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    skill = SkillSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    skill_id = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), source='skill', write_only=True
    )

    class Meta:
        model = LearningRequest
        fields = ['id','user','skill','desired_level', 'status','created_at','user_id','skill_id',]
        read_only_fields = ('created_at',)

class SwapRequestSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    provider = UserSerializer(read_only=True) 
    offer = TeachingOfferSerializer(read_only=True) 

    # Поля для ID при создании
    requester_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='requester', write_only=True
    )
    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='provider', write_only=True
    )
    offer_id = serializers.PrimaryKeyRelatedField(
        queryset=TeachingOffer.objects.all(), source='offer', write_only=True
    )

    class Meta:
        model = SwapRequest
        fields = ['id','requester','provider','offer','message','status','created_at','updated_at','requester_id','provider_id','offer_id',]
        read_only_fields = ('created_at', 'updated_at')