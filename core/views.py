from django.shortcuts import render, redirect
from .models import Pessoa     # importando o model Pessoa criado

# Create your views home a index.


# RAED
def home(request):
    pessoas = Pessoa.objects.all()   # Pegando todas as pessoas cadastradas pela view
    # enviando pro meu template atraves da variavel e valor ("pessoas": pessoas)
    return render(request, "index.html", {"pessoas": pessoas}) 


#CREATE
def salvar(request):
    # View tem a função de acessar os models para: (criar e ler ...) 
        # -> bate no banco e volta com dado 
            # -> Injeto o dado no template
                # -> Jogando a resposta de volta, neste caso a index.html

                # IMPRIMIR: Crio o dado pela view, pego a lista toda envio para index -> 
                    # -> No index faço um loop para pegar as pessoa para imprimir em tela

    vnome = request.POST.get("nome") # Pego o dado inserido do form via POST após o submit e guardei na variavel nome
    Pessoa.objects.create(nome=vnome) # Criei no BD o novo nome da nova pessoa 
    pessoas = Pessoa.objects.all()  # Agora evio uma lista atualizada de nomes para meu index
    return render(request, "index.html", {"pessoas":pessoas})  # e envia para meu forme


# EDITE
def editar(request, id):   
    #Editar recebe o ID da pessoa
    pessoa = Pessoa.objects.get(id=id)   # Pega o ID por pessoa pelo get
    return render(request, "update.html", {"pessoa": pessoa})


# READ UPDATE
def update(request, id):
    vnome = request.POST.get("nome")  # nome atualizado
    pessoa = Pessoa.objects.get(id=id) # pegar a pessoa do BD pq ela existe
    pessoa.nome = vnome  # o novo valor que veio do banco
    pessoa.save()
    return redirect(home)


# DELETE
def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)