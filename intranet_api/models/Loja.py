from django.db import models


class Loja(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    cep = models.IntegerField()
    cnpj = models.IntegerField()
    codigo = models.IntegerField()
    prefixo_ramal = models.IntegerField()