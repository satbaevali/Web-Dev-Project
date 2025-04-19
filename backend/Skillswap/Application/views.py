from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.http import Http404
from Application import models

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import SkillCategory, Skill, TeachingOffer, LearningRequest, SwapRequest
from accounts.models import User

from .serializer import (
    SkillCategorySerializer,
    SkillSerializer,
    TeachingOfferSerializer,
    LearningRequestSerializer,
    SwapRequestSerializer
)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class SkillCategoryViewSet(viewsets.ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().select_related('category')
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TeachingOfferViewSet(viewsets.ModelViewSet):
    queryset = TeachingOffer.objects.all().select_related('user', 'skill')
    serializer_class = TeachingOfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LearningRequestViewSet(viewsets.ModelViewSet):
    queryset = LearningRequest.objects.all().select_related('user', 'skill')
    serializer_class = LearningRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return LearningRequest.objects.filter(user=user)
        return LearningRequest.objects.none()

class SwapRequestViewSet(viewsets.ModelViewSet):
    queryset = SwapRequest.objects.all().select_related('requester', 'provider', 'offer')
    serializer_class = SwapRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return SwapRequest.objects.filter(
                models.Q(requester=user) | models.Q(provider=user)
            ).distinct()
        return SwapRequest.objects.none()
