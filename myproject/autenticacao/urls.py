from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutenticarViewSet, CadastroViewSet, StatusViewSet

router = DefaultRouter()
router.register(r'autenticar', AutenticarViewSet, basename='autenticar')
router.register(r'cadastro', CadastroViewSet, basename='cadastro')
router.register(r'status', StatusViewSet, basename='status')


urlpatterns = [
    path('', include(router.urls)),
]