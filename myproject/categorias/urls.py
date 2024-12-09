from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [
    # Outras rotas do seu projeto
    path('', include(router.urls)),
]