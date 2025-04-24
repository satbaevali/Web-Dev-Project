from rest_framework import serializers
from django.contrib.auth import get_user_model
from Application.models import Skill

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), required=False)

    def create(self, validated_data):
        # Извлекаем все нужные поля
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        skill = validated_data.get('skill', None)

        # Создаём пользователя
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.first_name = first_name
        user.last_name = last_name
        if skill:
            user.skill = skill
        user.save()
        return user

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Имя пользователя уже занято")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email уже используется")
        return value
class ProfileSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), required=False)
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.skill = validated_data.get('skill', instance.skill)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance
