from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.ver_perfil, name='ver_perfil'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
]