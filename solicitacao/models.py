from django.db import models

class Funcionario(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.EmailField('email')
    cargo = models.CharField('cargo', max_length=120)

    def __str__(self):
        return self.nome

class Solicitacao(models.Model):
    origem = models.CharField('origem', max_length=250)
    destino = models.CharField('destino', max_length=250)
    Funcionario = models.ForeignKey('Funcionario')
    data = models.DateTimeField('data')

    def __str__(self):
        return self.destino

class Veiculo(models.Model):
    placa = models.CharField('placa', max_length=8)
    marca = models.CharField('marca', max_length=20)
    modelo = models.CharField('modelo', max_length=100)
    ano = models.CharField('ano', max_length=4)

    def __str__(self):
        return self.modelo

class Motorista(models.Model):
    cnh = models.CharField('cnh', max_length=8)
    nome = models.CharField('nome', max_length=100)
    categoria = models.CharField('categoria', max_length=2)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    Veiculo = models.ForeignKey('Veiculo')
    Motorista = models.ForeignKey('Motorista')
    Solicitacao = models.ForeignKey('Solicitacao')
