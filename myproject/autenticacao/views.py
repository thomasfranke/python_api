from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers
from .serializers import AutenticarSerializer
from .serializers import CadastroSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class CadastroViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = CadastroSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AccessToken.for_user(user)
        return Response({
            'token': str(token),
        }, status=status.HTTP_201_CREATED)
        
class AutenticarViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = AutenticarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(username=serializer.validated_data['username']).first()
        if user and user.check_password(serializer.validated_data['password']):
            token = AccessToken.for_user(user)
            return Response({
                'message': 'Usuário autenticado com sucesso!',
                'username': user.username,
                'token': str(token)
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

class StatusViewSet(viewsets.ViewSet):
    [IsAuthenticated]

    def list(self, request):
        user = request.user
        return Response({
            'message': 'Usuário autenticado!',
            'username': user.username,
        }, status=status.HTTP_200_OK)