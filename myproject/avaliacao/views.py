from django.shortcuts import render, redirect, get_object_or_404
from .forms import AvaliacaoForm
from estabelecimento.models import Estabelecimento
from django.contrib.auth.decorators import login_required
from .models import Avaliacao, Estabelecimento

@login_required
def adicionar_avaliacao(request, id):
    estabelecimento = Estabelecimento.objects.get(id=id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user  # Define o usuário autenticado
            avaliacao.estabelecimento = estabelecimento
            avaliacao.save()
            return redirect('detalhe_estabelecimento', id=estabelecimento.id)
    else:
        form = AvaliacaoForm()

    return render(request, 'avaliacao/avaliacao_form.html', {'form': form, 'estabelecimento': estabelecimento})



def editar_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id, usuario=request.user)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('detalhe_estabelecimento', id=avaliacao.estabelecimento.id)
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'avaliacao/avaliacao_form.html', {'form': form, 'estabelecimento': avaliacao.estabelecimento})


def excluir_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id, usuario=request.user)
    estabelecimento_id = avaliacao.estabelecimento.id
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('detalhe_estabelecimento', id=estabelecimento_id)
    return render(request, 'avaliacao/confirmar_exclusao.html', {'avaliacao': avaliacao})