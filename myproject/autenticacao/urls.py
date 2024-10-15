from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutenticarViewSet
from .views import CadastroViewSet


router = DefaultRouter()
router.register(r'autenticar', AutenticarViewSet, basename='autenticar')
router.register(r'cadastro', CadastroViewSet, basename='cadastro')


urlpatterns = [
    path('', include(router.urls)),
]
