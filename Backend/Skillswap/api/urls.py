# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, # Можешь добавить, если нужна проверка токена
)

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user') # Read-only user list/detail
router.register(r'skill-categories', views.SkillCategoryViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'teaching-offers', views.TeachingOfferViewSet)
router.register(r'learning-requests', views.LearningRequestViewSet)
router.register(r'swap-requests', views.SwapRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/me/', views.ProfileView.as_view(), name='profile-me'), # URL for current user's profile
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]