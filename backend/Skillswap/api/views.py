from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import Skill,SkillCategory,SwapRequest,TeachingOffer,User
from .serializers import SkillSerializer, UserSerializer,SkillCategory,SkillCategorySerializers,SwapRequestSerializer,TeachingOfferSerializer
from rest_framework.response import Response
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_active_teaching_offers(request):
    if request.method == 'GET':
        active_offers = TeachingOffer.objects.filter(status='active').select_related(
            'user','skill'
        )
        serializer = TeachingOfferSerializer(active_offers,many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_swap_request(request):
    if request.method == 'POST':

        serializer = SwapRequestSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
     
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                 return Response({"error": f"error for save {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillCategoryListCreateAPIView(APIView):
 
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
 
        categories = SkillCategory.objects.all()
    
        serializer = SkillCategorySerializers(categories, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
       
        serializer = SkillCategorySerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillDetailAPIView(APIView):
 
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        skill = self.get_object(pk)
        serializer = SkillSerializer(skill, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        skill = self.get_object(pk)
        serializer = SkillSerializer(skill, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        skill = self.get_object(pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)