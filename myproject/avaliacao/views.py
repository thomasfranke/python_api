from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .models import Avaliacao, Estabelecimento
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Avaliacao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        estabelecimento_id = self.request.data.get('estabelecimento')
        estabelecimento = get_object_or_404(Estabelecimento, id=estabelecimento_id)
        serializer.save(usuario=self.request.user, estabelecimento=estabelecimento)