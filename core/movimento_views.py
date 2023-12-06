from django.views.generic import ListView, CreateView, UpdateView, DetailView
from core.models import Movimento, Cadastro
from django.urls import reverse_lazy
from django.shortcuts import redirect

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cadastros'] = Cadastro.objects.all()
        return context

    def form_valid(self, form):
        movimento = form.save(commit=False)
        movimento.cadastro = self.request.POST.get('cadastro_id')
        movimento.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('lista_movimentos')

# Editar Movimento
class EditarMovimentoView(UpdateView):
    model = Movimento
    fields = ['cadastro', 'endereco_evento', 'data_evento', 'observacoes']
    template_name = 'movimentos/editar_movimento.html'

    def get_success_url(self):
        return reverse_lazy('lista_movimentos')

# Adicione outras views conforme necessário...
