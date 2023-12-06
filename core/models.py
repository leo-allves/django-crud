from django.db import models

# Modelo para Cadastro
class Cadastro(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    sobrenome = models.CharField(max_length=100, db_index=True)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15, db_index=True)
    escolha_acompanhamento = models.CharField(max_length=100)
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

# Modelo para Endereço dos Cadastros
class EnderecoDosCadastros(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='enderecos')
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, db_index=True)
    estado = models.CharField(max_length=2, db_index=True)
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.endereco

# Modelo para Acompanhamento (para uso futuro)
class Acompanhamento(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='acompanhamentos')
    data_ligacao = models.DateField(db_index=True)
    resultado_acompanhamento = models.CharField(max_length=100)
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.cadastro} - {self.data_ligacao}"

# Modelo para Integração
class Integracao(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='integracoes')
    data_integracao = models.DateField(db_index=True)
    resultado = models.CharField(max_length=100)
    notas = models.TextField()
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.cadastro} - {self.data_integracao}"

# Modelo para Movimento
class Movimento(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='movimentos')
    endereco_evento = models.CharField(max_length=255)
    data_evento = models.DateField(db_index=True)
    observacoes = models.TextField()
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.cadastro} - {self.data_evento}"
