from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Perfil
from .serializers import PerfilSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)

    def list(self, request, *args, **kwargs):
        perfil = self.get_queryset().first()
        

        if perfil is not None:
            serializer = self.get_serializer(perfil)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Perfil não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    def partial_update(self, request, *args, **kwargs):
        perfil = self.get_queryset().first()
        
        if perfil is None:
            return Response({'detail': 'Perfil não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(perfil, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)