


from django.db import models
from django.utils import timezone
from django.conf import settings

class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Skill Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='skills',
        verbose_name="Category"
    )

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['name']

    def __str__(self):
        return self.name

class TeachingOffer(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    ]
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='teaching_offers', verbose_name="User")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='offered_by', verbose_name="Skill")
    description = models.TextField(verbose_name="Offer Description")
    experience_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True, null=True, verbose_name="Experience Level")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Teaching Offer"
        verbose_name_plural = "Teaching Offers"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} teaches {self.skill.name}"

class TeachingOfferManager(models.Manager):

    def active(self):
        # Returns only active teaching offers
        return self.get_queryset().filter(status='active')

    def offers_for_skill(self, skill_id):
        return self.active().filter(skill_id=skill_id)


class LearningRequest(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('fulfilled', 'Fulfilled'),
        ('archived', 'Archived'),
    ]
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='learning_requests', verbose_name="User")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='wanted_by', verbose_name="Desired Skill")
    desired_level = models.CharField(max_length=50, blank=True, null=True, verbose_name="Desired Level")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Learning Request"
        verbose_name_plural = "Learning Requests"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} wants to learn {self.skill.name}"

class SwapRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    requester = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='sent_swap_requests', verbose_name="Requester")
    provider = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='received_swap_requests', verbose_name="Provider")
    offer = models.ForeignKey(TeachingOffer, on_delete=models.CASCADE, related_name='swap_requests', verbose_name="Offer")
    message = models.TextField(blank=True, null=True, verbose_name="Message")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Swap Request"
        verbose_name_plural = "Swap Requests"
        ordering = ['-created_at']

    def __str__(self):
        return f"Request from {self.requester.username} to {self.provider.username} for {self.offer.skill.name}"

# Add Review, Conversation, Message models here if needed

class Review(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2,'⭐⭐'),
        (3,'⭐⭐⭐'),
        (4,'⭐⭐⭐⭐'),
        (5,'⭐⭐⭐⭐⭐'),
    ]
    reviewer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='given_reviews', verbose_name='Reviewer')
    reviewee = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name = 'received_reviews', verbose_name="Reviewee")
    teaching_offer = models.ForeignKey('TeachingOffer', on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews', verbose_name="Teaching Offer")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Rating")
    comment = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']
        unique_together = ('reviewer', 'reviewee', 'teaching_offer') # Один пользователь может оставить один отзыв одному преподавателю по одному предложению

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.reviewee.username}"

class Conversation(models.Model):
    """Модель для хранения информации о переписке между пользователями."""
    participants = models.ManyToManyField('accounts.User', related_name='conversations', verbose_name="Participants")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"
        ordering = ['-updated_at']
        # Можно добавить уникальность для пары участников, если это необходимо
        # unique_together = ('user1', 'user2')

        def __str__(self):
            return f"Conversation between {', '.join(p.username for p in self.participants.all())}"