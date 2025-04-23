from rest_framework import serializers
from django.contrib.auth import get_user_model
from Application.models import Skill

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'skill']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Заметьте: first_name, last_name и skill из validated_data сейчас игнорируются при создании пользователя
        return user



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','bio','skill','profile_picture']

    def update(self, instance, validated_data):
        # для каждого поля из validated_data присваиваем новое значение
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
