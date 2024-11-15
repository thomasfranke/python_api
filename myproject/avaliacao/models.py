from django.db import models
from django.contrib.auth.models import User
from estabelecimento.models import Estabelecimento

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, related_name='avaliacoes', on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.estabelecimento.nome} - Nota: {self.nota}"