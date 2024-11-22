from django.shortcuts import render, redirect, get_object_or_404
from .forms import AvaliacaoForm
from estabelecimento.models import Estabelecimento
from django.contrib.auth.decorators import login_required
from .models import Avaliacao, Estabelecimento

@login_required
def adicionar_avaliacao(request, id):
    estabelecimento = get_object_or_404(Estabelecimento, id=id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.estabelecimento = estabelecimento
            avaliacao.usuario = request.user
            avaliacao.save()
            # Redireciona para os detalhes do estabelecimento
            return redirect('detalhe_estabelecimento', id=estabelecimento.id)
    else:
        form = AvaliacaoForm()
    
    return render(request, 'avaliacao/avaliacao_form.html', {
        'form': form,
        'estabelecimento': estabelecimento,
        'range': range(1, 6),
    })

@login_required
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

@login_required
def excluir_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id, usuario=request.user)
    estabelecimento_id = avaliacao.estabelecimento.id
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('detalhe_estabelecimento', id=estabelecimento_id)
    return render(request, 'avaliacao/confirmar_exclusao.html', {'avaliacao': avaliacao})