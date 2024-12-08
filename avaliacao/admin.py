from django.contrib import admin
from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('estabelecimento', 'usuario', 'nota', 'comentario', 'data_criacao')
    list_filter = ('estabelecimento', 'nota', 'usuario')