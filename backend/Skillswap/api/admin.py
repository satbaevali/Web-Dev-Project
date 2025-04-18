# admin.py

from django.contrib import admin
from .models import SkillCategory,Skill,TeachingOffer,LearningRequest,SwapRequest
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
from .models import Review
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "bio", "profile_picture")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(User, UserAdmin)


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

    list_display = ('id', 'user_info', 'skill', 'status', 'experience_level', 'created_at')
    list_filter = ('status', 'experience_level', 'skill__category', 'skill')
    search_fields = ('user__name', 'user__first_name', 'user__last_name', 'skill__name', 'description')
    raw_id_fields = ('user', 'skill')
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('user', 'skill')

    
    def user_info(self, obj):
        return f"{obj.user.username} (ID: {obj.user.id})" 
    user_info.short_description = 'User'



@admin.register(LearningRequest)
class LearningRequestAdmin(admin.ModelAdmin):
 
    list_display = ('id', 'user_info', 'skill', 'status', 'created_at')
    list_filter = ('status', 'skill__category', 'skill')
    search_fields = ('user__name', 'user__first_name', 'user__last_name', 'skill__name')
    raw_id_fields = ('user', 'skill')
    readonly_fields = ('created_at',)
    list_select_related = ('user', 'skill')

    def user_info(self, obj):
        return f"{obj.user.username} (ID: {obj.user.id})" 
    user_info.short_description = 'User'


@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):

    list_display = ('id', 'requester_info', 'provider_info', 'offer_skill_name', 'status', 'created_at')
    list_filter = ('status', 'offer__skill__category')
    search_fields = ('requester__name', 'provider__name', 'offer__skill__name', 'message')
    raw_id_fields = ('requester', 'provider', 'offer')
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('requester', 'provider', 'offer', 'offer__skill')

    def requester_info(self, obj):
        return f"{obj.requester.username} (ID: {obj.requester.id})"
    requester_info.short_description = 'Requester'

    def provider_info(self, obj):
         return f"{obj.provider.username} (ID: {obj.provider.id})"
    provider_info.short_description = 'Provider'

    def offer_skill_name(self, obj):
        return obj.offer.skill.name
    offer_skill_name.short_description = 'Skill Offered'

admin.site.register(Review)