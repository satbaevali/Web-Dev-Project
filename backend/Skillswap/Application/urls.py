from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,
)
from accounts.views import LoginAPIView
from .views import (
    SkillCategoryViewSet, SkillViewSet, TeachingOfferViewSet,
    LearningRequestViewSet, SwapRequestViewSet, search_view, 
)

router = DefaultRouter()
router.register(r'skill-categories', SkillCategoryViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'teaching-offers', TeachingOfferViewSet)
router.register(r'learning-requests', LearningRequestViewSet)
router.register(r'swap-requests', SwapRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('search/', search_view, name='search'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]
