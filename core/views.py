from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Pessoa  # Importando o modelo Pessoa criado

# Sinal para executar antes de uma Pessoa ser salva
@receiver(pre_save, sender=Pessoa)
def minha_funcao_de_sinal(sender, instance, **kwargs):
    # Código para executar antes de uma Pessoa ser salva
    pass

# Função que lida com a exibição da página inicial
def home(request):
    pessoas = Pessoa.objects.all()  # Pegando todas as pessoas cadastradas
    return render(request, "index.html", {"pessoas": pessoas})

# Função para criar uma nova Pessoa
def salvar(request):
    if request.method == "POST":
        vnome = request.POST.get("nome")
        vemail = request.POST.get("email")
        Pessoa.objects.create(nome=vnome, email=vemail)  # Criando uma nova Pessoa no BD
        return redirect('home')  # Redirecionando para a página inicial
    else:
        return render(request, "index.html")

# Função para editar uma Pessoa existente
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, "update.html", {"pessoa": pessoa})

# Função para atualizar uma Pessoa
def update(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == "POST":
        pessoa.nome = request.POST.get("nome")
        pessoa.email = request.POST.get('email')
        pessoa.save()  # Salvando as alterações
        return redirect('home')  # Redirecionando para a página inicial
    else:
        return render(request, 'update.html', {'pessoa': pessoa})

# Função para deletar uma Pessoa
def delete(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == "POST":
        pessoa.delete()  # Deletando a Pessoa
    return redirect('home')  # Redirecionando para a página inicial após a deleção
