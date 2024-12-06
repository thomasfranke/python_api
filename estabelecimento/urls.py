from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstabelecimentoViewSet

router = DefaultRouter()
router.register(r'', EstabelecimentoViewSet, basename='estabelecimento')

urlpatterns = [
    path('', include(router.urls)),
]