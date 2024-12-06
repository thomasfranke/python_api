from django.urls import path
from estabelecimento.views import detalhe_estabelecimento
from . import views

app_name = 'avaliacao'

urlpatterns = [
    path('adicionar/<int:id>/', views.adicionar_avaliacao, name='adicionar_avaliacao'),
    path('editar/<int:id>/', views.editar_avaliacao, name='editar_avaliacao'),
    path('excluir/<int:id>/', views.excluir_avaliacao, name='excluir_avaliacao'),
    path('estabelecimento/<int:id>/', detalhe_estabelecimento, name='detalhe_estabelecimento'),
]