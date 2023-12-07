from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cadastro, EnderecoDosCadastros
from django.db import transaction
from django.contrib import messages

# Detalhes Cadastros
class DetalhesCadastroView(DetailView):
    model = Cadastro
    template_name = 'cadastro/detalhes_cadastro.html'
    context_object_name = 'cadastro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aqui você pode adicionar qualquer contexto adicional, como endereços, se necessário
        return context


# Listar Cadastros
class ListaCadastrosView(ListView):
    model = Cadastro
    template_name = 'cadastro/lista_cadastros.html'
    context_object_name = 'cadastros'

# Criar Cadastro
class CriarCadastroView(CreateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    template_name = 'cadastro/criar_cadastro.html'

    def form_valid(self, form):
        try:
            with transaction.atomic():
                cadastro = form.save()
                endereco = EnderecoDosCadastros(
                    cadastro=cadastro,
                    endereco=self.request.POST['endereco'],
                    numero=self.request.POST['numero'],
                    cep=self.request.POST['cep'],
                    bairro=self.request.POST['bairro'],
                    cidade=self.request.POST['cidade'],
                    estado=self.request.POST['estado']
                )
                endereco.save()
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

    def form_valid(self, form):
        try:
            with transaction.atomic():
                self.object = form.save()
                endereco = EnderecoDosCadastros.objects.get(cadastro=self.object)
                endereco.endereco = self.request.POST.get('endereco', endereco.endereco)
                endereco.numero = self.request.POST.get('numero', endereco.numero)
                endereco.cep = self.request.POST.get('cep', endereco.cep)
                endereco.bairro = self.request.POST.get('bairro', endereco.bairro)
                endereco.cidade = self.request.POST.get('cidade', endereco.cidade)
                endereco.estado = self.request.POST.get('estado', endereco.estado)
                endereco.save()
                messages.success(self.request, "Cadastro atualizado com sucesso!")
            return redirect(self.get_success_url())
        except Exception as e:
            messages.error(self.request, f"Erro ao atualizar cadastro: {e}")
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('lista_cadastros')

# Deletar Cadastro
class DeletarCadastroView(DeleteView):
    model = Cadastro
    template_name = 'cadastro/deletar_cadastro.html'
    success_url = reverse_lazy('lista_cadastros')
