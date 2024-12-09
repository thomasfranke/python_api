from django.urls import path
from .views import CadastroViewSet, AutenticarViewSet, LogoutViewSet, StatusViewSet
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('cadastro/', CadastroViewSet.as_view({'post': 'create'}), name='cadastro'),
    path('login/', LoginView.as_view(template_name='autenticacao/login.html'), name='login'),
    path('autenticar/', AutenticarViewSet.as_view({'post': 'create'}), name='autenticar'),
    path('logout/', LogoutViewSet.as_view({'post': 'create'}), name='logout'),
    path('status/', StatusViewSet.as_view({'get': 'list'}), name='status'),
]
