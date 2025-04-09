

from django.urls import path

from . import views

urlpatterns = [
    path('skill-categories/', views.SkillCategoryListCreateAPIView.as_view(), name='skill-category-list-create'),
    path('teaching-offers/active/', views.list_active_teaching_offers, name='active-teaching-offers-list'),
    path('skills/<int:pk>/', views.SkillDetailAPIView.as_view(), name='skill-detail'),

 
]