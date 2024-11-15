from django.urls import path
from . import views

app_name = 'avaliacao'

urlpatterns = [
    path('adicionar/<int:id>/', views.adicionar_avaliacao, name='adicionar_avaliacao'),
    path('<int:id>/editar/', views.editar_avaliacao, name='editar_avaliacao'),
    path('<int:id>/excluir/', views.excluir_avaliacao, name='excluir_avaliacao'),
]