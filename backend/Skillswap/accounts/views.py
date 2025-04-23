from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model
User = get_user_model()
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Имя пользователя и пароль обязательны!'}, status=status.HTTP_400_BAD_REQUEST)


        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'username': user.username
            })
        else:
            return Response({'error': 'Неверное имя пользователя или пароль'}, status=status.HTTP_401_UNAUTHORIZED)
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("DATA RECEIVED:", request.data) # Эта строка покажет, какие данные были получены
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(): # Здесь происходит проверка данных
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("ERRORS:", serializer.errors) # Если данные невалидны, сюда попадает сообщение об ошибке
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, username=None):  # <--- Добавили username
        try:
            user = User.objects.get(username=username) if username else request.user
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
class EditProfileAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        profile = request.user
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = request.user
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Профиль обновлен'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)