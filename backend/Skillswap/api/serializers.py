# api/serializers.py

from rest_framework import serializers
from accounts.models import User
from .models import  SkillCategory, Skill, TeachingOffer, LearningRequest, SwapRequest
# If you are using the built-in User model via settings.AUTH_USER_MODEL:
#from django.contrib.auth import get_user_model
#User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'profile_picture',
            'password', 
            'date_joined',
            'last_login',
        ]
        read_only_fields = ('date_joined', 'last_login')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}, 'required': False}
        }

    def create(self, validated_data):
        # Use the create_user method for proper handling, including password hashing
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Handle password update separately if provided
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class ProfileSerializer(serializers.ModelSerializer):
    # This serializer is often used for retrieving/updating the current user's profile
    class Meta:
        model = User
        # Exclude sensitive fields like password, is_staff, is_superuser, groups, user_permissions
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'profile_picture',
        ]
        read_only_fields = ('username', 'email', 'id') # Typically username/email aren't changed here


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ['id', 'name', 'description']

class SkillSerializer(serializers.ModelSerializer):
    category = SkillCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=SkillCategory.objects.all(),
        source='category',
        write_only=True,
        allow_null=True,
        required=False
    )

    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'category', 'category_id']

class TeachingOfferSerializer(serializers.ModelSerializer):
    # Use simplified User representation for nested display if needed
    # user = serializers.StringRelatedField(read_only=True) # Example: Shows user.__str__
    user = UserSerializer(read_only=True) # Shows full user profile based on UserSerializer
    skill = SkillSerializer(read_only=True)

    # For write operations, expect IDs
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    skill_id = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), source='skill', write_only=True
    )

    class Meta:
        model = TeachingOffer
        fields = [
            'id',
            'user',
            'skill',
            'description',
            'experience_level',
            'status',
            'created_at',
            'updated_at',
            'user_id',
            'skill_id',
        ]
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
        fields = [
            'id',
            'user',
            'skill',
            'desired_level',
            'status',
            'created_at',
            'user_id',
            'skill_id',
        ]
        read_only_fields = ('created_at',)


class SwapRequestSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    provider = UserSerializer(read_only=True)
    offer = TeachingOfferSerializer(read_only=True)

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
        fields = [
            'id',
            'requester',
            'provider',
            'offer',
            'message',
            'status',
            'created_at',
            'updated_at',
            'requester_id',
            'provider_id',
            'offer_id',
        ]
        read_only_fields = ('created_at', 'updated_at')

# Add ReviewSerializer, ConversationSerializer, MessageSerializer here if needed