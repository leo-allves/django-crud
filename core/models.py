from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadastro, EnderecoDosCadastros, Integracao, Movimento
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# CADASTROS

# Listar Cadastros
class ListaCadastrosView(ListView):
    model = Cadastro
    template_name = 'cadastros/lista_cadastros.html'
    context_object_name = 'cadastros'

# Criar Registro Integrado (Cadastro, Endereço e Integração)
class CriarRegistroIntegradoView(CreateView):
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

# Deletar Cadastro
class DeletarCadastroView(DeleteView):
    model = Cadastro
    template_name = 'cadastros/deletar_cadastro.html'
    success_url = reverse_lazy('lista_cadastros')

# Detalhes do Cadastro
def detalhes_cadastro(request, pk):
    context = {
        'cadastro': get_object_or_404(Cadastro, pk=pk),
        'endereco': get_object_or_404(EnderecoDosCadastros, cadastro=pk),
        'integracao': get_object_or_404(Integracao, cadastro=pk)
    }
    return render(request, 'cadastros/detalhes_cadastro.html', context)

# MOVIMENTO

# Listar Movimentos
class ListaMovimentosView(ListView):
    model = Movimento
    template_name = 'movimentos/listar_movimento.html'

# Detalhes do Movimento
class DetalhesMovimentoView(DetailView):
    model = Movimento
    template_name = 'movimentos/detalhes_movimento.html'

# Criar Movimento
class CriarMovimentoView(CreateView):
    model = Movimento
    fields = ['cadastro', 'endereco_evento', 'data_evento', 'observacoes']
    template_name = 'movimentos/cadastrar_movimento.html'
    success_url = reverse_lazy('lista_movimentos')

# Atualizar Movimento
class AtualizarMovimentoView(UpdateView):
    model = Movimento
    fields = ['cadastro', 'endereco_evento', 'data_evento', 'observacoes']
    template_name = 'movimentos/editar_movimento.html'
    success_url = reverse_lazy('lista_movimentos')

# Deletar Movimento
class DeletarMovimentoView(DeleteView):
    model = Movimento
    template_name = 'movimentos/deletar_movimento.html'
    success_url = reverse_lazy('lista_movimentos')
