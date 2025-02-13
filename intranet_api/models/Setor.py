from django.db import models
from . import Loja

class Setor(models.Model):
    nome = models.CharField(max_length=30)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nome)