from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from core.models import Movimento, Cadastro
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

# Listar Movimentos
class ListaMovimentosView(ListView):
    model = Movimento
    template_name = 'movimento/listar_movimento.html'
    context_object_name = 'movimentos'  # Adicionei context_object_name para consistência

# Detalhes do Movimento
class DetalhesMovimentoView(DetailView):
    model = Movimento
    template_name = 'movimento/detalhes_movimento.html'

# Criar Movimento
class CriarMovimentoView(CreateView):
    model = Movimento
    fields = ['cadastro', 'endereco_evento', 'data_evento', 'observacoes']
    template_name = 'movimento/cadastrar_movimento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cadastros'] = Cadastro.objects.all()  # Fornecer a lista de cadastros para o formulário
        return context

    def form_valid(self, form):
        form.instance.cadastro = get_object_or_404(Cadastro, pk=self.request.POST.get('cadastro'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listar_movimento')

# Editar Movimento
class EditarMovimentoView(UpdateView):
    model = Movimento
    fields = ['cadastro', 'endereco_evento', 'data_evento', 'observacoes']
    template_name = 'movimento/editar_movimento.html'

    def get_success_url(self):
        return reverse_lazy('listar_movimento')

# Deletar Movimento
class DeletarMovimentoView(DeleteView):
    model = Movimento
    template_name = 'movimento/deletar_movimento.html'  # Corrigido o caminho do template
    success_url = reverse_lazy('listar_movimento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Movimento'
        return context
