from django.db import models   # model reposavel por criar o model já dentro da migration

# Create your models here.

class Pessoa(models.Model):    # Model no django e como eu crio dados no BD
    nome = models.CharField(max_length=100)  # uma vez criado posso registrar no admin.py


    # função que define a visibilidade no BD pelo valor
        # Exemplo imprime a pessoa Marcos e não object1 ...
    def __str__(self) -> str:
        return self.nome
    