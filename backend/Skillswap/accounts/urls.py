


from django.urls import include,path
from .views import ProfileAPIView,EditProfileAPIView

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('edit_profile/',EditProfileAPIView.as_view(), name='edit_profile' ),

]