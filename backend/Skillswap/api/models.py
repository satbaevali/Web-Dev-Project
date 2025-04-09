from django.db import models
from django.utils import timezone
class User(models.Model):
    name = models.CharField(max_length=255,unique=True,blank=True)
    email = models.CharField(max_length=255,unique=True,blank=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    profile_picture = models.URLField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

class SkillCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.name
class Skill(models.Model):
    name = models.CharField(max_length=150,unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(SkillCategory,on_delete=models.CASCADE,null=True,blank=True,related_name='skills')

    def __str__(self):
        return self.name
# Модель Предложения Обучить
class TeachingOffer(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Начинающий'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый'),
        ('expert', 'Эксперт'),
        ]
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('inactive', 'Неактивно'),
        ('archived', 'В архиве'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teaching_offers')
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE,related_name='offered_by')
    description  = models.TextField()
    experience_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} teaches {self.skill.name}"

class LearningRequest(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активен'),
        ('fulfilled', 'Выполнен'),
        ('archived', 'В архиве'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learning_requests')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='wanted_by')
    desired_level = models.CharField(max_length=50, blank=True, null=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} wants to learn {self.skill.name}"

# Модель Запроса на Обмен/Урок
class SwapRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_swap_requests')
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_swap_requests')
    offer = models.ForeignKey(TeachingOffer, on_delete=models.CASCADE, related_name='swap_requests') 
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request from {self.requester.username} to {self.provider.username} for {self.offer.skill.name}"



