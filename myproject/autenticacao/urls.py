from django.urls import path
from .views import CadastroViewSet, AutenticarViewSet, LogoutViewSet, StatusViewSet

urlpatterns = [
    path('cadastro/', CadastroViewSet.as_view({'post': 'create'}), name='cadastro'),
    path('autenticar/', AutenticarViewSet.as_view({'post': 'create'}), name='autenticar'),
    path('logout/', LogoutViewSet.as_view({'post': 'create'}), name='logout'),
    path('status/', StatusViewSet.as_view({'get': 'list'}), name='status'),
]
