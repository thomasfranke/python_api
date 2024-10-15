from django.db import models

class Autenticacao(models.Model):
    name = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.name
