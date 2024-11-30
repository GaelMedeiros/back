from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.descricao} - R$ {self.preco:.2f} - {self.quantidade}"


