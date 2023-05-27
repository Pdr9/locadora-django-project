from django.shortcuts import render, redirect
from locadora.models import Locacao, Filme
from locadora.forms import LocacaoForm, FilmeForm
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def listar_locacoes(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locacao.html', {'locacoes': locacoes})

def criar_locacao(request):
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_locacoes')
    else:
        form = LocacaoForm()
    return render(request, 'criar_locacao.html', {'form': form})

def editar_locacao(request, id):
    locacao = Locacao.objects.get(id=id)
    if request.method == 'POST':
        form = LocacaoForm(request.POST, instance=locacao)
        if form.is_valid():
            form.save()
            return redirect('listar_locacoes')
    else:
        form = LocacaoForm(instance=locacao)
    return render(request, 'editar_locacao.html', {'form': form, 'locacao': locacao})

    

def excluir_locacao(request, id):
    locacao = Locacao.objects.get(id=id)
    locacao.delete()
    return redirect('listar_locacoes')

def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes.html', {'filmes': filmes})

def criar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()
    return render(request, 'criar_filme.html', {'form': form})

def editar_filme(request, id):
    filme = Filme.objects.get(id=id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'editar_filme.html', {'form': form})

def excluir_filme(request, id):
    filme = Filme.objects.get(id=id)
    filme.delete()
    return redirect('listar_filmes')