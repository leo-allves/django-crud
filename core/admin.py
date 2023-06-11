from django.contrib import admin
from .models import Pessoa  # importo a class o medel criado

# Register your models here.

admin.site.register(Pessoa)   # registro o model que eu quero que apareça