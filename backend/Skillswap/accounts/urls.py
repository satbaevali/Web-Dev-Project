


from django.urls import include,path
from .views import ProfileAPIView,EditProfileAPIView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('edit_profile/',EditProfileAPIView.as_view(), name='edit_profile' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)