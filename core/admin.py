# core/admin.py

from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')  # Certifique-se de que 'email' está incluído aqui.