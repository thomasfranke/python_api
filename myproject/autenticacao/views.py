from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers
from .serializers import AutenticarSerializer
from .serializers import CadastroSerializer


class CadastroViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()  # Define um queryset vazio
    serializer_class = CadastroSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'id': user.id}, status=status.HTTP_201_CREATED)

class AutenticarViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = AutenticarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(username=serializer.validated_data['username']).first()
        if user and user.check_password(serializer.validated_data['password']):
            return Response({'message': 'Usuário autenticado com sucesso!', 'id': user.id}, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
