from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Cadastro, EnderecoDosCadastros, Integracao
from django.db import transaction
from django.contrib import messages


# Listar Cadastros
class ListaCadastrosView(ListView):
    model = Cadastro
    template_name = 'cadastro/lista_cadastros.html'
    context_object_name = 'cadastros'

    def get_queryset(self):
        # Substitua 'all' por um método de filtragem se necessário
        return Cadastro.objects.all().prefetch_related('enderecos', 'integracoes')

# Criar Cadastro
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.db import transaction
from .models import Cadastro, EnderecoDosCadastros, Integracao

class CriarCadastroView(CreateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    template_name = 'cadastro/criar_cadastro.html'

    def form_valid(self, form):
        try:
            with transaction.atomic():
                # Salva o cadastro principal
                cadastro = form.save()

                # Cria e salva o endereço associado
                endereco = EnderecoDosCadastros(
                    cadastro=cadastro,
                    endereco=self.request.POST.get('endereco'),
                    numero=self.request.POST.get('numero'),
                    cep=self.request.POST.get('cep'),
                    bairro=self.request.POST.get('bairro'),
                    cidade=self.request.POST.get('cidade'),
                    estado=self.request.POST.get('estado')
                )
                endereco.save()

                # Cria e salva os dados de integração associados
                integracao = Integracao(
                    cadastro=cadastro,
                    data_integracao=self.request.POST.get('data_integracao'),
                    resultado=self.request.POST.get('resultado'),
                    notas=self.request.POST.get('notas')
                )
                integracao.save()

                messages.success(self.request, "Cadastro criado com sucesso!")
                return redirect(self.get_success_url())
        except Exception as e:
            messages.error(self.request, f"Erro ao criar cadastro: {e}")
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')

    model = Cadastro
    fields = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    template_name = 'cadastro/criar_cadastro.html'

    def form_valid(self, form):
        try:
            with transaction.atomic():
                # Salva o cadastro principal
                cadastro = form.save()

                # Cria e salva o endereço associado
                endereco = EnderecoDosCadastros(
                    cadastro=cadastro,
                    endereco=self.request.POST.get('endereco'),
                    numero=self.request.POST.get('numero'),
                    cep=self.request.POST.get('cep'),
                    bairro=self.request.POST.get('bairro'),
                    cidade=self.request.POST.get('cidade'),
                    estado=self.request.POST.get('estado')
                )
                endereco.save()

                # Cria e salva os dados de integração associados
                integracao = Integracao(
                    cadastro=cadastro,
                    data_integracao=self.request.POST.get('data_integracao'),
                    resultado=self.request.POST.get('resultado'),
                    notas=self.request.POST.get('notas')
                )
                integracao.save()

                messages.success(self.request, "Cadastro criado com sucesso!")
                return redirect(self.get_success_url())
        except Exception as e:
            messages.error(self.request, f"Erro ao criar cadastro: {e}")
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')


# Atualizar Cadastro
class AtualizarCadastroView(UpdateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    template_name = 'cadastro/editar_cadastro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cadastro_id = self.kwargs.get('pk')
        # Aqui, se o endereço ou a integração não existirem, eles serão criados com valores padrão.
        context['endereco'], _ = EnderecoDosCadastros.objects.get_or_create(
            cadastro_id=cadastro_id,
            defaults={'endereco': 'Endereço padrão', 'numero': 0, 'cep': '00000-000', 'bairro': 'Bairro padrão', 'cidade': 'Cidade padrão', 'estado': 'SP'}
        )
        context['integracao'], _ = Integracao.objects.get_or_create(
            cadastro_id=cadastro_id,
            defaults={'data_integracao': '1900-01-01', 'resultado': 'Resultado padrão', 'notas': 'Notas padrão'}
        )
        return context

    def form_valid(self, form):
        # Primeiro, chama o form_valid do form para garantir que o cadastro é válido
        self.object = form.save()
        endereco = EnderecoDosCadastros.objects.get(cadastro=self.object)
        integracao = Integracao.objects.get(cadastro=self.object)

        # Certifica-se de que os dados do POST estão presentes antes de tentar atribuí-los
        endereco.endereco = self.request.POST.get('endereco', endereco.endereco)
        endereco.numero = self.request.POST.get('numero', endereco.numero)
        endereco.cep = self.request.POST.get('cep', endereco.cep)
        endereco.bairro = self.request.POST.get('bairro', endereco.bairro)
        endereco.cidade = self.request.POST.get('cidade', endereco.cidade)
        endereco.estado = self.request.POST.get('estado', endereco.estado)
        endereco.save()

        integracao.data_integracao = self.request.POST.get('data_integracao', integracao.data_integracao)
        integracao.resultado = self.request.POST.get('resultado', integracao.resultado)
        integracao.notas = self.request.POST.get('notas', integracao.notas)
        integracao.save()

        # Redireciona para a URL de sucesso
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('detalhes_cadastro', kwargs={'pk': self.object.pk})




# Detalhes do Cadastro
class DetalhesCadastroView(DetailView):
    model = Cadastro
    template_name = 'cadastro/detalhes_cadastro.html'
    context_object_name = 'cadastro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['endereco'] = get_object_or_404(EnderecoDosCadastros, cadastro=self.object)
        context['integracao'] = get_object_or_404(Integracao, cadastro=self.object)
        return context

# Deletar Cadastro
class DeletarCadastroView(DeleteView):
    model = Cadastro
    template_name = 'cadastro/deletar_cadastro.html'
    success_url = reverse_lazy('lista_cadastros')
