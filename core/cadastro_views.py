from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
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
        cadastro = form.save()
        EnderecoDosCadastros.objects.create(cadastro=cadastro, **self.request.POST)
        Integracao.objects.create(cadastro=cadastro, **self.request.POST)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')

# Atualizar Cadastro
class AtualizarCadastroView(UpdateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    template_name = 'cadastros/editar_cadastro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cadastro_id = self.kwargs.get('pk')
        context['endereco'] = get_object_or_404(EnderecoDosCadastros, cadastro_id=cadastro_id)
        context['integracao'] = get_object_or_404(Integracao, cadastro_id=cadastro_id)
        return context

    def form_valid(self, form):
        cadastro = form.save()
        endereco = get_object_or_404(EnderecoDosCadastros, cadastro=cadastro)
        integracao = get_object_or_404(Integracao, cadastro=cadastro)

        # Atualiza EnderecoDosCadastros e Integracao
        for attr, value in self.request.POST.items():
            setattr(endereco, attr, value) if hasattr(endereco, attr) else None
            setattr(integracao, attr, value) if hasattr(integracao, attr) else None

        endereco.save()
        integracao.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')
    

# Detalhes do Cadastro
class DetalhesCadastroView(DetailView):
    model = Cadastro
    template_name = 'cadastros/detalhes_cadastro.html'
    context_object_name = 'cadastro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cadastro = self.get_object()
        context['endereco'] = get_object_or_404(EnderecoDosCadastros, cadastro=cadastro)
        context['integracao'] = get_object_or_404(Integracao, cadastro=cadastro)
        return context
    

# Deletar Cadastro
class DeletarCadastroView(DeleteView):
    model = Cadastro
    template_name = 'cadastros/deletar_cadastro.html'
    success_url = reverse_lazy('lista_cadastros')

# Adicione outras views conforme necessário
