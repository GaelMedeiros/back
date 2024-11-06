from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

    descricao = models.CharField(max_length=15)

    preco = models.CharField(max_length=60)

    quantidade= models.CharField(max_length=60)

    def __str__(self):
        return self.nome

