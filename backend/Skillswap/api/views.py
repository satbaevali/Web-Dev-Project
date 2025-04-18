from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.http import Http404
from api import models
from rest_framework.decorators import action



from django.contrib.auth import get_user_model
User = get_user_model()

from .models import SkillCategory, Skill, TeachingOffer, LearningRequest, SwapRequest
from accounts.models import User

from .serializers import (
    UserSerializer,
    ProfileSerializer,
    SkillCategorySerializer,
    SkillSerializer,
    TeachingOfferSerializer,
    LearningRequestSerializer,
    SwapRequestSerializer
)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "User registered successfully", "user_id": user.id, "username": user.username},
            status=status.HTTP_201_CREATED
        )

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['status'] # Add filter for status

    @action(detail=False, methods=['get'])
    def active(self, request):
        active_offers = self.get_queryset().filter(status='active')
        serializer = self.get_serializer(active_offers, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LearningRequestViewSet(viewsets.ModelViewSet):
    queryset = LearningRequest.objects.all().select_related('user', 'skill')
    serializer_class = LearningRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['status'] 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        active_offers = self.get_queryset().filter(status='active')
        serializer = self.get_serializer(active_offers, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return LearningRequest.objects.filter(user=user)
        return LearningRequest.objects.none()

class SwapRequestViewSet(viewsets.ModelViewSet):
    queryset = SwapRequest.objects.all().select_related('requester', 'provider', 'offer')
    serializer_class = SwapRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return SwapRequest.objects.filter(
                models.Q(requester=user) | models.Q(provider=user)
            ).distinct()
        return SwapRequest.objects.none()
