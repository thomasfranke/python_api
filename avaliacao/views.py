from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Avaliacao, Estabelecimento
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Lista apenas as avaliações do usuário autenticado
        return Avaliacao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # Define o usuário autenticado e o estabelecimento
        estabelecimento_id = self.request.data.get('estabelecimento')
        estabelecimento = get_object_or_404(Estabelecimento, id=estabelecimento_id)
        serializer.save(usuario=self.request.user, estabelecimento=estabelecimento)

    @action(detail=True, methods=['delete'], permission_classes=[permissions.IsAuthenticated])
    def excluir(self, request, pk=None):
        # Excluir uma avaliação
        avaliacao = get_object_or_404(Avaliacao, id=pk, usuario=request.user)
        avaliacao.delete()
        return Response({"detail": "Avaliação excluída com sucesso."}, status=204)