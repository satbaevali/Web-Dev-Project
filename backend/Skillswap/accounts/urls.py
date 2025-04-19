


from django.urls import include,path
from .views import edit_profile,profile

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),

]