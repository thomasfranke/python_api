from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import AutenticarSerializer
from .serializers import CadastroSerializer
from perfil.models import Perfil


from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model


User = get_user_model()

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = CadastroSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Perfil.objects.create(usuario=user)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': str(token),
        }, status=status.HTTP_201_CREATED)

        
class AutenticarViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = AutenticarSerializer
    def create(self, request):
        serializer = AutenticarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(username=serializer.validated_data['username']).first()
        if user and user.check_password(serializer.validated_data['password']):
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Usuário autenticado com sucesso!',
                'username': user.username,
                'token': str(token)
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)


class StatusViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        return Response({
            'message': 'Usuário autenticado!',
            'username': user.username,
        }, status=status.HTTP_200_OK)
        
class LogoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            token = Token.objects.get(usuario=request.user)
            token.delete()
            return Response({
                'message': 'Logout realizado com sucesso!'
            }, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({
                'message': 'Token não encontrado.'
            }, status=status.HTTP_400_BAD_REQUEST)