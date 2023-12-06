# core/admin.py

from django.contrib import admin
from core.models import Cadastro, EnderecoDosCadastros, Integracao, Movimento
# from core.models import Acompanhamento

# Registrando cada modelo para que eles apareçam na interface do admin do Django.

class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'idade', 'telefone', 'escolha_acompanhamento']
    search_fields = ['nome', 'sobrenome', 'telefone']
    list_filter = ['idade', 'escolha_acompanhamento']

class EnderecoDosCadastrosAdmin(admin.ModelAdmin):
    list_display = ['cadastro', 'endereco', 'cidade', 'estado']
    search_fields = ['cidade', 'estado']
    list_filter = ['cidade', 'estado']

class IntegracaoAdmin(admin.ModelAdmin):
    list_display = ['cadastro', 'data_integracao', 'resultado', 'notas']
    search_fields = ['cadastro__nome', 'cadastro__sobrenome']
    list_filter = ['data_integracao', 'resultado']

class MovimentoAdmin(admin.ModelAdmin):
    list_display = ['cadastro', 'endereco_evento', 'data_evento', 'observacoes']
    search_fields = ['cadastro__nome', 'cadastro__sobrenome', 'endereco_evento']
    list_filter = ['data_evento']

# Registrando os modelos com o Django admin
admin.site.register(Cadastro, CadastroAdmin)
admin.site.register(EnderecoDosCadastros, EnderecoDosCadastrosAdmin)
admin.site.register(Integracao, IntegracaoAdmin)
admin.site.register(Movimento, MovimentoAdmin)

# Futura inclusão:
# admin.site.register(Acompanhamento, AcompanhamentoAdmin)
# class AcompanhamentoAdmin(admin.ModelAdmin):
#     list_display = ['cadastro', 'data_ligacao', 'resultado_acompanhamento']
#     search_fields = ['cadastro__nome', 'cadastro__sobrenome']
#     list_filter = ['data_ligacao']