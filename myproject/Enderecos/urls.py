from django.urls import path
from .views import criar_endereco_view, listar_enderecos_view, atualizar_endereco_view, deletar_endereco_view, obter_endereco_view

urlpatterns = [
    path('criar/', criar_endereco_view, name='criar_endereco'),  # URL para criar um endereço
    path('', listar_enderecos_view, name='enderecos'),  # URL para listar endereços
    path('atualizar/<int:pk>/', atualizar_endereco_view, name='atualizar_endereco'),  # URL para atualizar um endereço
    path('deletar/<int:pk>/', deletar_endereco_view, name='deletar_endereco'),  # URL para deletar um endereço
    path('<int:pk>/', obter_endereco_view, name='obter_endereco'),  # URL para obter um endereço por ID
]