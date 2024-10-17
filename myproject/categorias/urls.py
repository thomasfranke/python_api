from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_categorias, name='listar_categorias'),
    path('nova/', views.criar_categoria, name='criar_categoria'),
    path('editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
]