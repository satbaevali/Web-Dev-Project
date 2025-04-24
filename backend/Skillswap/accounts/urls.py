


from django.urls import include,path
from .views import login_view, register_view, profile_view, edit_profile_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,
)
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/',edit_profile_view, name='edit_profile' ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/<str:username>/',profile_view, name='profile'),
    path('edit_profile/<str:username>/',edit_profile_view, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)