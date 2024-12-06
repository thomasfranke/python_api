from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', null=True)
    nome = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __str__(self):
        return f'{self.usuario.username} - {self.endereco}'
