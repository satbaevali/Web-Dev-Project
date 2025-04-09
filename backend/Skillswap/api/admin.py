# admin.py

from django.contrib import admin
from .models import User,SkillCategory,Skill,TeachingOffer,LearningRequest,SwapRequest

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'first_name', 'last_name', 'date_joined', 'last_login')
    search_fields = ('name', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login') 
    readonly_fields = ('date_joined', 'last_login', 'password')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}), 
        ('Personal info', {'fields': ('first_name', 'last_name', 'bio', 'profile_picture')}),
        ('Permissions', {'fields': ()}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

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
        return f"{obj.user.name} (ID: {obj.user.id})" 
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
        return f"{obj.user.name} (ID: {obj.user.id})" 
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
        return f"{obj.requester.name} (ID: {obj.requester.id})"
    requester_info.short_description = 'Requester'

    def provider_info(self, obj):
         return f"{obj.provider.name} (ID: {obj.provider.id})"
    provider_info.short_description = 'Provider'

    def offer_skill_name(self, obj):
        return obj.offer.skill.name
    offer_skill_name.short_description = 'Skill Offered'