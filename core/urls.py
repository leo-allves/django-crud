from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete

urlpatterns = [
    # path('', home),
    path('', home, name = 'home'),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),   # pegar ID
    path('update/<int:id>', update, name="update"),   # onde será impresso a página editada
    path('delete/<int:id>', delete, name="delete"),
]