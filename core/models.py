from django.shortcuts import render, redirect, get_object_or_404
# from core.models import Cadastro, EnderecoDosCadastros, Integracao, Movimento
from .models import Cadastro, EnderecoDosCadastros, Integracao, Movimento
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# -------------------------------------------------------------
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
        # Aqui você precisa salvar o Cadastro antes de poder criar os objetos relacionados.
        self.object = form.save()
        # Crie um objeto EnderecoDosCadastros relacionado.
        EnderecoDosCadastros.objects.create(
            cadastro=self.object,
            endereco=self.request.POST.get('endereco'),
            numero=self.request.POST.get('numero'),
            cep=self.request.POST.get('cep'),
            bairro=self.request.POST.get('bairro'),
            cidade=self.request.POST.get('cidade'),
            estado=self.request.POST.get('estado'),
        )
        # Crie um objeto Integracao relacionado.
        Integracao.objects.create(
            cadastro=self.object,
            data_integracao=self.request.POST.get('data_integracao'),
            resultado=self.request.POST.get('resultado_integracao'),
            notas=self.request.POST.get('notas_integracao'),
        )
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')

# Atualizar Registro Integrado (não incluído neste exemplo, mas seria similar ao CriarRegistroIntegradoView)

# Deletar Cadastro
class DeletarCadastroView(DeleteView):
    model = Cadastro
    template_name = 'cadastros/deletar_cadastro.html'
    context_object_name = 'cadastro'
    success_url = reverse_lazy('lista_cadastros')

    def delete(self, request, *args, **kwargs):
        # Sobrescrever o método delete para também deletar objetos relacionados, se necessário.
        # Se você estiver usando o `on_delete=models.CASCADE`, isso pode não ser necessário.
        self.get_object().delete()
        return redirect(self.success_url)

# Função para ver detalhes do Cadastro (opcional)
def detalhes_cadastro(request, pk):
    cadastro = get_object_or_404(Cadastro, pk=pk)
    endereco = get_object_or_404(EnderecoDosCadastros, cadastro=pk)
    integracao = get_object_or_404(Integracao, cadastro=pk)
    return render(request, 'cadastros/detalhes_cadastro.html', {
        'cadastro': cadastro,
        'endereco': endereco,
        'integracao': integracao
    })


# -------------------------------------------------------------

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
