from django.db import models
from django.contrib.auth.models import User
from estabelecimento.models import Estabelecimento
from django.core.validators import MinValueValidator, MaxValueValidator

class Avaliacao(models.Model):
    estabelecimento = models.ForeignKey(
        'estabelecimento.Estabelecimento',
        on_delete=models.CASCADE,
        related_name='avaliacoes'  # Isso cria o atributo avaliacoes em Estabelecimento
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, related_name='avaliacoes', on_delete=models.CASCADE)
    comentario = models.TextField(max_length=200)  # Limite de 200 caracteres
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    data_criacao = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.estabelecimento.nome} - Nota: {self.nota}"