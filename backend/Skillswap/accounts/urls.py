


from django.urls import include,path
from .views import ProfileAPIView,EditProfileAPIView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,
)
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('edit_profile/',EditProfileAPIView.as_view(), name='edit_profile' ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/<str:username>/', ProfileAPIView.as_view(), name='profile'),
    path('edit_profile/<str:username>/', EditProfileAPIView.as_view(), name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)