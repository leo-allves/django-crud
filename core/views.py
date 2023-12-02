from django.shortcuts import render, redirect, get_object_or_404
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

    if request.method == "POST":
        vnome = request.POST.get("nome") # Pego o dado inserido do form via POST após o submit e guardei na variavel nome
        vemail = request.POST.get("email")
        Pessoa.objects.create(nome=vnome, email=vemail) # Criei no BD o novo nome da nova pessoa 
        return redirect('home') # e envia para meu forme
    else:
        return render(request, "index.html")

# EDIT
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, "update.html", {"pessoa": pessoa})

# READ UPDATE
def update(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == "POST":
        pessoa.nome = request.POST.get("nome")  # nome atualizado
        pessoa.email = request.POST.get('email')  # email atualizado
        pessoa.save()
        return redirect('home')  # certifique-se de que 'home' é o nome correto da sua URL
    else:
        # Se não for um POST, mostre o formulário com os dados atuais da pessoa
        return render(request, 'update.html', {'pessoa': pessoa})



# DELETE
def delete(request, id):
    if request.method == "POST":
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.delete()
    return redirect('home')
