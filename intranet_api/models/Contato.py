from django.db import models
from . import Setor,Loja


class Contato(models.Model):
    nome = models.CharField(max_length=60)
    ramal = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["setor"]
        verbose_name_plural = "Contatos"