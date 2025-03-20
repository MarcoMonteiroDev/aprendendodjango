from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=20)
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    descricao = models.TextField()

    def __str__ (self):
        return self.nome