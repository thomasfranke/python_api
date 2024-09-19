from django.db import models

class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    dt_nasc = models.DateField(null=True, blank=True)

