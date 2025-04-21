# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from Application.models import Skill  # импортируем модель Skill

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True, verbose_name="Bio")
    profile_picture = models.URLField(blank=True, null=True, verbose_name="Profile picture URL")
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True, related_name='users', verbose_name="Skill")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
