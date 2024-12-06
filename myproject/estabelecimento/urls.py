from django.urls import path
from .views import listar_estabelecimentos, criar_estabelecimento, editar_estabelecimento, deletar_estabelecimento, detalhe_estabelecimento

urlpatterns = [
    path('', listar_estabelecimentos, name='listar_estabelecimentos'),
    path('criar/', criar_estabelecimento, name='criar_estabelecimento'),
    path('editar/<int:id>/', editar_estabelecimento, name='editar_estabelecimento'),
    path('deletar/<int:id>/', deletar_estabelecimento, name='deletar_estabelecimento'),
    path('detalhes/<int:id>/', detalhe_estabelecimento, name='detalhe_estabelecimento'),
]