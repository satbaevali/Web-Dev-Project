from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import (
    SkillCategory, Skill, TeachingOffer, LearningRequest,
    SwapRequest, Review, Conversation,
    # Message
)


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
        fields = ['id', 'name', 'description', 'category', 'category_id','price','image']

class TeachingOfferSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    skill = SkillSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )
    skill_id = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        source='skill',
        write_only=True
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
    user = serializers.StringRelatedField(read_only=True)
    skill = SkillSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )
    skill_id = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        source='skill',
        write_only=True
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
    requester = serializers.StringRelatedField(read_only=True)
    provider = serializers.StringRelatedField(read_only=True)
    offer = TeachingOfferSerializer(read_only=True)

    requester_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='requester',
        write_only=True
    )
    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='provider',
        write_only=True
    )
    offer_id = serializers.PrimaryKeyRelatedField(
        queryset=TeachingOffer.objects.all(),
        source='offer',
        write_only=True
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

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)
    reviewee = serializers.StringRelatedField(read_only=True)
    teaching_offer = serializers.StringRelatedField(read_only=True)

    reviewer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='reviewer',
        write_only=True
    )
    reviewee_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='reviewee',
        write_only=True
    )
    teaching_offer_id = serializers.PrimaryKeyRelatedField(
        queryset=TeachingOffer.objects.all(),
        source='teaching_offer',
        write_only=True,
        allow_null=True,
        required=False
    )


    class Meta:
        model = Review
        fields = [
            'id',
            'reviewer',
            'reviewee',
            'teaching_offer',
            'rating',
            'comment',
            'created_at',
            'updated_at',
            'reviewer_id',
            'reviewee_id',
            'teaching_offer_id',
        ]
        read_only_fields = ('created_at', 'updated_at')

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'id',
            'participants',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ('created_at', 'updated_at')


