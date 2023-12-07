from django.urls import path
from django.views.generic import RedirectView
from . import cadastro_views, movimento_views

urlpatterns = [
    # Redireciona a rota raiz para 'lista_cadastros'
    path('', RedirectView.as_view(url='/cadastro/', permanent=False), name='index'),

    # CADASTROS
    path('cadastro/', cadastro_views.ListaCadastrosView.as_view(), name='lista_cadastros'),
    path('cadastro/novo/', cadastro_views.CriarCadastroView.as_view(), name='criar_cadastro'),
    path('cadastro/editar/<int:pk>/', cadastro_views.AtualizarCadastroView.as_view(), name='editar_cadastro'),
    path('cadastro/detalhes/<int:pk>/', cadastro_views.DetalhesCadastroView.as_view(), name='detalhes_cadastro'),
    path('cadastro/deletar/<int:pk>/', cadastro_views.DeletarCadastroView.as_view(), name='deletar_cadastro'),

    # MOVIMENTOS (se necessário no projeto)
    path('movimento/', movimento_views.ListaMovimentosView.as_view(), name='lista_movimentos'),
    path('movimento/novo/', movimento_views.CriarMovimentoView.as_view(), name='cadastrar_movimento'),
    path('movimento/editar/<int:pk>/', movimento_views.EditarMovimentoView.as_view(), name='editar_movimento'),
    path('movimento/detalhes/<int:pk>/', movimento_views.DetalhesMovimentoView.as_view(), name='detalhes_movimento'),
    path('movimento/deletar/<int:pk>/', movimento_views.DeletarMovimentoView.as_view(), name='deletar_movimento'),
]
