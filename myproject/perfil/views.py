from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfil
from .forms import PerfilForm

# View para exibir o perfil do usuário
def ver_perfil(request, id):
    perfil = get_object_or_404(Perfil, id=id)
    return render(request, 'perfil/ver_perfil.html', {'perfil': perfil})

# View para editar o perfil do usuário
def editar_perfil(request):
    perfil = Perfil.objects.get(user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil', id=perfil.id)
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil/editar_perfil.html', {'form': form})