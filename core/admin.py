# core/admin.py

from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')  # Campos que você quer mostrar na lista

    # As permissões padrão já permitem todas as ações para superusuários.
    # Os métodos a seguir são para controle fino, se necessário.

    def has_add_permission(self, request):
        # Permite adicionar novas Pessoas
        return True

    # def has_change_permission(self, request, obj=None):
    #     # Permite a alteração de Pessoas existentes
    #     return True

    # def has_delete_permission(self, request, obj=None):
    #     # Permite deletar Pessoas
    #     return True

    # Se você deseja adicionar uma visualização detalhada personalizada, você pode sobrescrever get_urls ou adicionar um método get_readonly_fields, por exemplo.

