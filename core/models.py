from django.db import models

# Modelo para Cadastro
class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)
    escolha_acompanhamento = models.CharField(max_length=100, blank=True)
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

# Modelo para Endereço dos Cadastros
class EnderecoDosCadastros(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='enderecos')
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)  # Alterado de IntegerField para CharField
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.endereco

# Modelo para Integração
class Integracao(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='integracoes')
    data_integracao = models.DateField()
    resultado = models.CharField(max_length=100)
    notas = models.TextField(blank=True)
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.cadastro} - {self.data_integracao}"

# Modelo para Movimento (se necessário)
class Movimento(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='movimentos')
    endereco_evento = models.CharField(max_length=255)
    data_evento = models.DateField()
    observacoes = models.TextField(blank=True)
    dat_inc = models.DateTimeField(auto_now_add=True)
    dat_exc = models.DateTimeField(null=True, blank=True)
    dat_aut = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.cadastro} - {self.data_evento}"
