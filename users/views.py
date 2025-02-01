from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from requests import Response

from common.authentication import APIKeyAuthentication
from common.permissions import HasAPIKey, IsAdminUser, IsOperatorUser
from users.serializers import UserSerializer
from .models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.views import APIView

class UserByCodeView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser | IsOperatorUser]

    def get(self, request, code):
        user = get_object_or_404(User, code=code)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, code):
        user = get_object_or_404(User, code=code)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code):
        user = get_object_or_404(User, code=code)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def check_object_permissions(self, request, obj):
        if request.method == 'DELETE' and not request.user.is_admin:
            self.permission_denied(request, message="You do not have permission to delete this object.")
        super().check_object_permissions(request, obj)

@csrf_exempt
@api_view(['POST'])
@authentication_classes([]) 
@permission_classes([AllowAny])
def verify_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return JsonResponse({
            'message': 'User logged in successfully',
            'access_token': access_token,
            'refresh_token': refresh_token
        })
    else:
        return JsonResponse({'message': 'Invalid username or password'}, status=400)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def register(request):
    user_data = request.data
    user = User.objects.create_user(
        username=user_data['username'],
        password=user_data['password']
    )
    user.first_name = user_data['first_name']
    user.last_name = user_data['last_name']
    user.email = user_data['email']
    user.telegram_username = user_data['telegram_username']
    user.phone_number = user_data['phone_number']
    user.save()
    
    user_data = UserSerializer(user).data
    return JsonResponse(user_data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def me(request):
    user = get_object_or_404(User, id=request.user.id)
    user_data = UserSerializer(user).data
    return JsonResponse(user_data)