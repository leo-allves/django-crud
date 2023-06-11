# Comandos projeto crud django

### 1 - Criar venv : Nos ajuda a isolar e gerenciar mais de um projeto e versões diferentes do django
    - Ex: 1 cliente usa django 2 outro a versão 4 ....
    - São ambiente virtuais que isola a versão d ecada cliente

        ````python

            python -m venv cliente1

        ````

    - Após entrar na pasta e ativar esta venv
    - acessar via terminal a pasta /Scripts/activate.bate
    - após criar a venv sempre terá está estrutura e deve ser ativada
    - Assim que for ativado o nome da pasta venv criada ficará dentro de parenteses
    Ex: (cliente1) 

        ````python

            projrto_criado/Scripts/activate

        ````

### 2 - Instalar o Django
    - pip é uma ferramenta que vem junto ao instalar o python

        ````python

            pip install django

        ````
    - Após instalar o django:
        - Vamos criar um projeto Django
        - basicamente chamamos "django-admin startproject nome-do-projeto"

        ````python

            django-admin startproject app .  

            # neste caso app é nome do projeto que escolhi
            # o (.) para que pegue somente o que está dentro do cliente1

        ````

### OBS: Após rodar tudo
    - O arquivos
    manage.py : É um utilitario onde será usado para rodar comandos do django
    Pasta app/  : Onde está o 
        > settings.py : Que está os arquivos de configuração do nosso sistema
        > urls.py : Onde fica as rotas do nosso sistema

### 3 - Levantando ambiente
    - Rodando comando (runserver) a partir do nosso manage.py para rodar o projeto
    - Após será informado o caminho para acessra no browser
        > http://127.0.0.1:8000/

        ````python

            python manage.py runserver 

        ````
    - Após acessar o cmainho:
        http://127.0.0.1:8000/ o ambiente será aberto
    - Acessando o ambiente admin que vem por padrão urls.py dentro do projeto criado
        http://127.0.0.1:8000/admin
        Ex: app/urls.py
            - Aqui estará o caminho "path('admin/', admin.site/urls)"
    
### 4 - Criando a tabelas (migrate) a partir da configuração de BD do projeto/settings.py
        - Neste caso o projeto se chama app sendo o caminho "app/settings.py"
        - por padrão vem coinfigurado para rodar no SQLlite3
        - caso utilize outro banco será necessario alterar as configurações
        Após verificar está parte rodar o comando (migrate) em nosso arquivo de comandos django manage.py

        ````python

            python manage.py migrate

        ````

    - Após criar um super usuario admin, para acessar
    - PASSOS

````python

    # 1º criar o super usuario admin
        python manage.py createsuperuser admin

    # 2º setar as configurações do usuario admin criado
        python manage.py createsuperuser

        # Aparecerá para setar username, email, password os cmapos

    # 3º rodar o ambiente novamente 
        python manage.py runserver

    # 4º para acessar a parte admin 
        http://127.0.0.1:8000/admin

````


## INICIANDO O CRUD (CRUD = Create, Read, Update, Delete)

### 1 - CRIANDO APPs
    - rodando startapp 
        Que cria varias apps dentro do nosso sistema(projeto criado)
        Neste exemplo criamos uma chamada "core"
        Mas pode ser criada uma para clientes, outra para produto, checauout, entrega ....
        OBS: Cada app deve ser reponsável por cada parte d emeu sistema

````python

    python manage.py startapp core

````

    - Testando url nova com hello world

````python

    # 1º ir na pasta do projeto neste caso app/urls.py
        # incluir ao lado do path um include no from
            # Após incluir a url no "urlpatterns"

                from django.contrib import admin
                from django.urls import path, include

                urlpatterns = [
                    path("admin/", admin.site.urls),
                    path('core/', include('core.urls'))
                ]

    # 2º importar a url criada no app/urls.py para o modulo core criado
        # Criar um arquivo urls.py dentro da pasta core
            # Dar uma olhada na estrutura (django request workflow)
        # Colar praticamente a estrutura da app/urls.py
            # Adicionar o caminho para View atraves do from
                from django.contrib import admin
                from django.urls import path, include
                from .views import home

                urlpatterns = [
                    path('core/', include('core.urls'))
                ]

    # 3º acessar a pasta do modulo no caso core/view.py
        # usando o tamplete render criar uma função e apontar para o arquivo html
            from django.shortcuts import render

            # Create your views here.
            def home(request):
                return render(request, "index.html") 

    # 4º acessar novamente o app/urls.py e editar a urlpatterns
        # Neste caso o caminho, toda vez que eu chamar core/ será direcionado para home
            # Neste caso coloco vazia pois será minha index
                from django.shortcuts import render

                # Create your views here.
                from django.contrib import admin
                from django.urls import path, include
                from .views import home

                urlpatterns = [
                    path('', home)
                ]
        
    # 5º Criar o arquivo index.html
        # Desta forma dentro da pasta core(modelo)
            # Criar uma pasta templates/index.html

    # 6º Para rodar toda vez que crio um modulo(aplicação) preciso registrar ele nas configurações gerais do sistema (app/settings.py)
        # ir em INSTALLED_APPS e adicionar como no exemplo abaixo, após rodar ambiente

            INSTALLED_APPS = [
                "django.contrib.admin",
                "django.contrib.auth",
                "django.contrib.contenttypes",
                "django.contrib.sessions",
                "django.contrib.messages",
                "django.contrib.staticfiles",
                "core"
            ]
````


### 2 - Começando CRUD - READ

    - Acessar a aplicação no caso core/models.py

````python
        #core/models.py

            from django.db import models

            # Create your models here.

            class Pessoa(models.Model):    # Model no django e como eu crio dados no BD
                nome = models.CharField(max_lenght=100)   # uma vez criado posso registrar no admin.py
````

    - registrar em app/admin.py para que apareça ao acessar a parte admin no navegador

````py
    #core/admin.py

        from django.contrib import admin
        from .models import Pessoa  # importo a class o medel criado

        # Register your models here.
        admin.site.register(Pessoa)  # registro o model que eu quero que apareça

````

    - Rodar no terminal para criar evoluir o BD da core/migrations criando o model que criei Pessoa

````py
    #terminal

        python manage.py makemigrations

        # irá mostrar o retorno que foi criado um novo model dentro da pasta migration/
            # até aqui ele não criou nada no banco ainda só o arquivo na migrations

        Migrations for 'core'
            core\migrations\0001_initial.py
            - Crate model Pessoa

    # após rodar o comando magrate
        # agora sim será criado no BD

        python manage.py migrate

    # rodar o comando para subir o servidor runserver e verificar se foi criado
        # http://127.0.0.1:8000/admin

        python manage.py runserver

    
    # adicionar a função que dará visibilidade do valor inserido

        from django.db import models   # model reposavel por criar o model já dentro da migration

        # Create your models here.

        class Pessoa(models.Model):    # Model no django e como eu crio dados no BD
            nome = models.CharField(max_length=100)  # uma vez criado posso registrar no admin.py


            # função que define a visibilidade no BD pelo valor
                # Exemplo imprime a pessoa Marcos e não object1 ...
            def __str__(self) -> str:
                return self.nome

````

    - Criando app/vews.py
        - importar a model criada
            from.models import Pessoa
        - pegar todas as pessoas que forem cadastradas pela view
            pessoas = Pessoa.objects.all()

        ````python
        # app/views.py

            from django.shortcuts import render
            from .models import Pessoa     # importando o model Pessoa criado

            # Create your views here.
            def home(request):
                pessoas = Pessoa.objects.all()   # Pegando todas as pessoas cadastradas pela view
                # enviando pro meu template atraves da variavel e valor ("pessoas": pessoas)
                return render(request, "index.html", {"pessoas": pessoas}) 

        ````

    - Dentro do meu tamplate (app/template) agora tenho acesso as pessoas

        ````html
        # app/template/index.html

            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <!-- Usando djinja é uma linguagem de templates que dá possibilidades 
                de manipular dados que vem do back-and,imprimindo e pegando a var da view por ex -->
                <ul>
                    {% for pessoa in pessoas %}                      <!-- {% %} para comandos -->             
                        <li>{{ pessoa.id }} - {{ pessoa.nome }}</li> <!-- {{ }} para variaveis -->   
                    {% endfor %}
                </ul>
            </body>
            </html>

        ````    

### 3 - Começando CRUD - CREATE
        - Criando o formulário no arquivo core/templates/index.html
            - Deve ser criado um formulário
                > Após clicar no botão ele irá dar submit do meu forme é enviar os dados do 
                input para a view que vai estar amarrada a minha url: salvar
                

                ````html
                <body>
                    <ul>
                        {% for pessoa in pessoas %}                      <!-- {% %} para comandos -->             
                            <li>{{ pessoa.id }} - {{ pessoa.nome }}</li> <!-- {{ }} para variaveis -->   
                        {% endfor %}
                    </ul>

                    <form action="{% url 'salvar' %}"> <!-- Criando url salvar quando der submit -->
                        {% csrf_token %} <!-- para proteção do form -->
                        <input type="text" name="nome">
                            <!-- Após clicar no botão ele irá dar submit do meu forme é enviar os dados do 
                            input para a view que vai estar amarrada a minha url: salvar-->
                        <button type="submit">Salvar</button> 
                    </form>
                </body>


                <!-- O {% csrf_token %} 
                    * É valida se ao slavar o dado e legitimo evitamos fraude e ataques hacker

                    * Ao inspecionar você verá que ele gera um codigo criptografado de validação ex:
                    <input type="hidden" name="csrfmiddlewaretoken" value="xC2am00twmqVgWciHCjmvhh4CXvaSOqzVXXkiNiG29OKbTbUhXovvpfuVTh2RNBN">
                -->
                
                ````

            - Após criação do form, devo criar está rota e amarrar a url: 'salvar' a minha view

            ````py
            # core/urls.py

                from django.contrib import admin
                from django.urls import path, include
                from .views import home, salvar    # importando view salvar

                urlpatterns = [
                    path('', home),
                    path('salvar/', salvar, name="salvar"),  # criando url com nome salvar e caminho
                ]

            # Após isso ir na view e criar ela

            # core/views.py

                from django.shortcuts import render
                from .models import Pessoa     # importando o model Pessoa criado

                # Create your views home a index.
                def home(request):
                    pessoas = Pessoa.objects.all()   # Pegando todas as pessoas cadastradas pela view
                    # enviando pro meu template atraves da variavel e valor ("pessoas": pessoas)
                    return render(request, "index.html", {"pessoas": pessoas}) 

                # Create your views salvar após sumit do formulario core/tempaltes/index.html.
                def salvar(request):

                # View tem a função de acessar os models para: (criar e ler ...) 
                    # -> bate no banco e volta com dado 
                        # -> Injeto o dado no template
                            # -> Jogando a resposta de volta, neste caso a index.html

                            # IMPRIMIR: Crio o dado pela view, pego a lista toda envio para index -> 
                                # -> No index faço um loop para pegar as pessoa para imprimir em tela

                #Criar
                nome = request.POST.get("nome") # Pego o dado inserido do form via POST após o submit e guardei na variavel nome
                Pessoa.objects.create(nome=nome) # Criei no BD o novo nome da nova pessoa 

                # Ler com dados atualizados
                pessoas = Pessoa.objects.all()  # Agora evio uma lista atualizada de nomes para meu index
                return render(request, "index.html", {"pessoas":pessoas})  # e envia para meu forme
            ````


### 3 - Começando CRUD - EDITAR

    - Primeiro criar uma url e um link editar no form

        ````html
            <!-- core/tempaltes/index.html -->
            <li>{{ pessoa.id }} - {{ pessoa.nome }} <a href="{% url 'editar' pessoa.id %}">Editar</a></li>
        ````

        - Segundo criar a rota em urls.py

            ````py
                # core/urls.py

                from .views import home, salvar, editar

                urlpatterns = [
                    path('', home),
                    path('salvar/', salvar, name="salvar"),
                    path('editar/<int:id>', editar, name="editar"),  # pegar ID
                ]
            ````

        - Terceiro criar a view

            ````py
                # core/views.py

                def editar(request, id):
                #Editar
                pessoa = Pessoa.objects.get(id=id)   # pegar pessoa por ID
                return render(request, "update.html", {"pessoa": pessoa})
            ````

        - 4º criar template/update.html

            ````html
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>

                    {{pessoa.id}} - {{ pessoa.nome }}

                    <form action="{% url 'update' pessoa.id %}" method="POST"> <!-- Criando url salvar quando der submit -->
                        {% csrf_token %} <!-- para proteção do form -->
                        <input type="text" name="nome" value="{{pessoa.nome}}">
                            <!-- Após clicar no botão ele irá dar submit do meu forme é enviar os dados do 
                            input para a view que vai estar amarrada a minha url: salvar-->
                        <button type="submit">Update</button> 
                    </form>

                </body>
                </html>
            ````

        - 5ª criar a url update em core/urls.py ...

            ````python

                from django.contrib import admin
                from django.urls import path, include
                from .views import home, salvar, editar, update

                urlpatterns = [
                    path('', home),
                    path('salvar/', salvar, name="salvar"),
                    path('editar/<int:id>', editar, name="editar"),   # pegar ID
                    path('update/', update, name="update"),   # onde será impresso a página editada
                ]
            ````

        - 6ª criar a função na view para carregar o campo editado
   
            ````python

                # impor a view update após cria a função

                # READ UPDATE
                def update(request, id):
                    vnome = request.POST.get("nome")  # nome atualizado
                    pessoa = Pessoa.objects.get(id=id) # pegar a pessoa do BD pq ela existe
                    pessoa.nome = vnome  # o novo valor que veio do banco
                    pessoa.save()
                    return redirect(home)
                
            ````


### 4 - Começando CRUD - DELETE

    - Primeiro criar uma url e um link editar no form

        ````html
            <!-- core/tempaltes/index.html -->
            <ul>
                {% for pessoa in pessoas %}                    
                    <li>{{ pessoa.id }} - {{ pessoa.nome }} 
                        <a href="{% url 'editar' pessoa.id %}">Editar</a>
                        <a href="{% url 'delete' pessoa.id %}">Deletar</a>
                    </li>
                {% endfor %}
            </ul>
        ````

        - Segundo criar a rota em urls.py

            ````py
                # core/urls.py

                from django.contrib import admin
                from django.urls import path, include
                from .views import home, salvar, editar, update, delete

                urlpatterns = [
                    path('', home),
                    path('salvar/', salvar, name="salvar"),
                    path('editar/<int:id>', editar, name="editar"),   # pegar ID
                    path('update/<int:id>', update, name="update"),   # onde será impresso a página editada
                    path('delete/<int:id>', delete, name="delete"),
                ]
            ````

        - Terceiro criar a view e após deleção redirecionar para home

            ````py
                # core/views.py

                # DELETE
                def delete(request, id):
                    pessoa = Pessoa.objects.get(id=id)
                    pessoa.delete()
                    return redirect(home)
            ````

        