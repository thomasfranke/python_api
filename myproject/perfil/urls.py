from django.urls import path
from . views import ver_perfil_view, editar_perfil_view

urlpatterns = [
    path('perfil/<int:id>/', ver_perfil_view, name='ver_perfil'),
    path('perfil/editar/', editar_perfil_view, name='editar_perfil'),
]