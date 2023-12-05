from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cadastro, EnderecoDosCadastros, Integracao

# Listar Cadastros
class ListaCadastrosView(ListView):
    model = Cadastro
    template_name = 'cadastros/lista_cadastros.html'
    context_object_name = 'cadastros'

# Criar Cadastro
class CriarCadastroView(CreateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    template_name = 'cadastros/criar_cadastro.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Criação de EnderecoDosCadastros e Integracao associados
        endereco = EnderecoDosCadastros(
            cadastro=self.object,
            endereco=self.request.POST.get('endereco'),
            numero=self.request.POST.get('numero'),
            cep=self.request.POST.get('cep'),
            bairro=self.request.POST.get('bairro'),
            cidade=self.request.POST.get('cidade'),
            estado=self.request.POST.get('estado')
        )
        endereco.save()

        integracao = Integracao(
            cadastro=self.object,
            data_integracao=self.request.POST.get('data_integracao'),
            resultado=self.request.POST.get('resultado_integracao'),
            notas=self.request.POST.get('notas_integracao')
        )
        integracao.save()

        return response

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')

# Atualizar Cadastro
class AtualizarCadastroView(UpdateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    template_name = 'cadastros/editar_cadastro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['endereco'] = get_object_or_404(EnderecoDosCadastros, cadastro=self.object)
        context['integracao'] = get_object_or_404(Integracao, cadastro=self.object)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        endereco = get_object_or_404(EnderecoDosCadastros, cadastro=self.object)
        integracao = get_object_or_404(Integracao, cadastro=self.object)

        # Atualização dos dados de EnderecoDosCadastros e Integracao
        endereco.endereco = self.request.POST.get('endereco')
        endereco.numero = self.request.POST.get('numero')
        endereco.cep = self.request.POST.get('cep')
        endereco.bairro = self.request.POST.get('bairro')
        endereco.cidade = self.request.POST.get('cidade')
        endereco.estado = self.request.POST.get('estado')
        endereco.save()

        integracao.data_integracao = self.request.POST.get('data_integracao')
        integracao.resultado = self.request.POST.get('resultado_integracao')
        integracao.notas = self.request.POST.get('notas_integracao')
        integracao.save()

        return response

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')

# Deletar Cadastro
class DeletarCadastroView(DeleteView):
    model = Cadastro
    template_name = 'cadastros/deletar_cadastro.html'
    success_url = reverse_lazy('lista_cadastros')

# Adicione outras views conforme necessário
