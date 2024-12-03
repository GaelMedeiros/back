from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')  # A imagem será armazenada na pasta 'produtos/'

    def __str__(self):
        return self.nome