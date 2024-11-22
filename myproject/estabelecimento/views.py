from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Estabelecimento
from .serializers import EstabelecimentoSerializer

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Estabelecimento.objects.all().order_by('id')

    def listAll(self, request, *args, **kwargs):
        estabelecimentos = self.get_queryset()
        serializer = self.get_serializer(estabelecimentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        estabelecimento = self.get_object()
        serializer = self.get_serializer(estabelecimento)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        estabelecimento = self.get_object()
        serializer = self.get_serializer(estabelecimento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        estabelecimento = self.get_object()
        estabelecimento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
