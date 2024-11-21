from django.shortcuts import render, redirect, get_object_or_404
from .forms import AvaliacaoForm
from estabelecimento.models import Estabelecimento
from django.contrib.auth.decorators import login_required
from .models import Avaliacao, Estabelecimento


def adicionar_avaliacao(request, id):
    estabelecimento = get_object_or_404(Estabelecimento, id=id)
    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.estabelecimento = estabelecimento
            avaliacao.usuario = request.user
            avaliacao.save()
            return redirect('detalhes_estabelecimento', id=id)
    else:
        form = AvaliacaoForm()
    
    return render(request, 'avaliacao/avaliacao_form.html', {
        'form': form,
        'estabelecimento': estabelecimento,
        'range': range(1, 6)  # Adiciona o range de 1 a 5
    })



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