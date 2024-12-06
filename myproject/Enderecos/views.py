from django.shortcuts import render, get_object_or_404, redirect
from .models import Endereco
from .forms import EnderecoForm

def listar_enderecos_view(request):
    enderecos = Endereco.objects.all()  # Recupera todos os endereços
    return render(request, 'enderecos/listar_enderecos.html', {'enderecos': enderecos})

def criar_endereco_view(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o endereço no banco de dados
            return redirect('enderecos')  # Redireciona para a lista de endereços após o sucesso
    else:
        form = EnderecoForm()

    return render(request, 'enderecos/criar_endereco.html', {'form': form})

def atualizar_endereco_view(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)  # Obtém o endereço a ser atualizado
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)  # Passa a instância do endereço
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('enderecos')  # Redireciona para a lista de endereços após a atualização
    else:
        form = EnderecoForm(instance=endereco)  # Preenche o formulário com os dados existentes

    return render(request, 'enderecos/atualizar_endereco.html', {'form': form, 'endereco': endereco})

def deletar_endereco_view(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)  # Obtém o endereço a ser deletado
    if request.method == 'POST':
        endereco.delete()  # Deleta o endereço
        return redirect('enderecos')  # Redireciona para a lista de endereços após a deleção

    return render(request, 'enderecos/deletar_endereco.html', {'endereco': endereco})

def obter_endereco_view(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)  # Obtém o endereço pelo ID
    return render(request, 'enderecos/obter_endereco.html', {'endereco': endereco})