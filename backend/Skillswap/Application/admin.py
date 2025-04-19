from django.contrib import admin
from .models import (
    SkillCategory, Skill, TeachingOffer, LearningRequest,
    SwapRequest, Review, Conversation
)
from django.contrib.auth import get_user_model # Импортируем User модель через get_user_model

# Получаем фактическую модель пользователя
User = get_user_model()

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category__name')
    list_select_related = ('category',)

@admin.register(TeachingOffer)
class TeachingOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_link', 'skill', 'status', 'experience_level', 'created_at')
    list_filter = ('status', 'experience_level', 'skill__category', 'skill')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'skill__name', 'description')
    raw_id_fields = ('user', 'skill')
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('user', 'skill')

    # Метод для отображения ссылки на пользователя в списке
    def user_link(self, obj):
        # Если пользователь существует, создаем ссылку на страницу администрирования пользователя
        if obj.user:
            from django.urls import reverse
            from django.utils.html import format_html
            link = reverse("admin:%s_%s_change" % (User._meta.app_label, User._meta.model_name), args=[obj.user.id])
            return format_html('<a href="{}">{} ({})</a>', link, obj.user.username, obj.user.id)
        return "-"
    user_link.short_description = 'User'


@admin.register(LearningRequest)
class LearningRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_link', 'skill', 'status', 'created_at')
    list_filter = ('status', 'skill__category', 'skill')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'skill__name')
    raw_id_fields = ('user', 'skill')
    readonly_fields = ('created_at',)
    list_select_related = ('user', 'skill')

    # Переиспользуем метод user_link из TeachingOfferAdmin или напишем аналог
    def user_link(self, obj):
        if obj.user:
            from django.urls import reverse
            from django.utils.html import format_html
            link = reverse("admin:%s_%s_change" % (User._meta.app_label, User._meta.model_name), args=[obj.user.id])
            return format_html('<a href="{}">{} ({})</a>', link, obj.user.username, obj.user.id)
        return "-"
    user_link.short_description = 'User'


@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'requester_link', 'provider_link', 'offer_skill_name', 'status', 'created_at')
    list_filter = ('status', 'offer__skill__category')
    search_fields = ('requester__username', 'provider__username', 'offer__skill__name', 'message')
    raw_id_fields = ('requester', 'provider', 'offer')
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('requester', 'provider', 'offer', 'offer__skill')

    def requester_link(self, obj):
        if obj.requester:
            from django.urls import reverse
            from django.utils.html import format_html
            link = reverse("admin:%s_%s_change" % (User._meta.app_label, User._meta.model_name), args=[obj.requester.id])
            return format_html('<a href="{}">{} ({})</a>', link, obj.requester.username, obj.requester.id)
        return "-"
    requester_link.short_description = 'Requester'

    def provider_link(self, obj):
        if obj.provider:
            from django.urls import reverse
            from django.utils.html import format_html
            link = reverse("admin:%s_%s_change" % (User._meta.app_label, User._meta.model_name), args=[obj.provider.id])
            return format_html('<a href="{}">{} ({})</a>', link, obj.provider.username, obj.provider.id)
        return "-"
    provider_link.short_description = 'Provider'

    def offer_skill_name(self, obj):
        return obj.offer.skill.name if obj.offer and obj.offer.skill else "-"
    offer_skill_name.short_description = 'Skill Offered'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'reviewer_link', 'reviewee_link', 'rating', 'teaching_offer', 'created_at')
    list_filter = ('rating', 'reviewee', 'teaching_offer')
    search_fields = ('comment', 'reviewer__username', 'reviewee__username', 'teaching_offer__description', 'teaching_offer__skill__name')
    raw_id_fields = ('reviewer', 'reviewee', 'teaching_offer')
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('reviewer', 'reviewee', 'teaching_offer', 'teaching_offer__skill')

    def reviewer_link(self, obj):
        if obj.reviewer:
            from django.urls import reverse
            from django.utils.html import format_html
            link = reverse("admin:%s_%s_change" % (User._meta.app_label, User._meta.model_name), args=[obj.reviewer.id])
            return format_html('<a href="{}">{} ({})</a>', link, obj.reviewer.username, obj.reviewer.id)
        return "-"
    reviewer_link.short_description = 'Reviewer'

    def reviewee_link(self, obj):
        if obj.reviewee:
            from django.urls import reverse
            from django.utils.html import format_html
            link = reverse("admin:%s_%s_change" % (User._meta.app_label, User._meta.model_name), args=[obj.reviewee.id])
            return format_html('<a href="{}">{} ({})</a>', link, obj.reviewee.username, obj.reviewee.id)
        return "-"
    reviewee_link.short_description = 'Reviewee'


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_participants', 'created_at', 'updated_at')
    list_filter = ('participants',) # Фильтрация по участникам
    # search_fields = ('participants__username',) # Поиск по именам участников - может быть неэффективным для ManyToMany
    readonly_fields = ('created_at', 'updated_at')

    def display_participants(self, obj):
        # Отображаем имена участников беседы
        return ", ".join([user.username for user in obj.participants.all()])
    display_participants.short_description = 'Participants'