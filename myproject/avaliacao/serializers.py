from rest_framework import serializers
from .models import Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'estabelecimento', 'usuario', 'comentario', 'nota', 'data_criacao', 'atualizado_em']
        read_only_fields = ['id', 'usuario', 'data_criacao', 'atualizado_em']