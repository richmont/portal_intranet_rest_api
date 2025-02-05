from django.db import models


class Loja(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=90)
    cep = models.IntegerField()
    cnpj = models.CharField(max_length=14)
    codigo = models.IntegerField()
    prefixo_ramal = models.IntegerField()
