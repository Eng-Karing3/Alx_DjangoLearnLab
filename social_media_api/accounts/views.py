from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import RegisterSerializer, UserSerializer, ProfileUpdateSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data.get('username'))
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Registration successful.',
            'token': token.key,
            'user': UserSerializer(user, context={'request': request}).data
        })


class LoginView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Uses DRF's serializer for username/password validation
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'message': 'Login successful.',
            'token': token.key,
            'user': UserSerializer(token.user, context={'request': request}).data
        })


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    GET /profile -> your profile
    PUT/PATCH /profile -> update email, bio, profile_picture
    """
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user, context={'request': request}).data)
