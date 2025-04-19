from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,
)

from .views import (
    SkillCategoryViewSet, SkillViewSet, TeachingOfferViewSet,
    LearningRequestViewSet, SwapRequestViewSet, 
    
)

router = DefaultRouter()


router.register(r'skill-categories', SkillCategoryViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'teaching-offers', TeachingOfferViewSet)
router.register(r'learning-requests', LearningRequestViewSet)
router.register(r'swap-requests', SwapRequestViewSet)

urlpatterns = [
    
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]