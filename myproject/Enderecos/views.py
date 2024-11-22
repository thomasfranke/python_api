from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Endereco.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        enderecos = self.get_queryset()
        serializer = self.get_serializer(enderecos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        endereco = self.get_object()
        serializer = self.get_serializer(endereco)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        endereco = self.get_object()
        serializer = self.get_serializer(endereco, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        endereco = self.get_object()
        endereco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
