from django.db import models
""" usar nome da classe no sigular se nao fica estranho """
class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=6)
    estoque = models.IntegerField("Quantidade em Estoque")
    def __str__(self):
        return f'{self.nome} estoque {self.estoque}'

    
class Cliente(models.Model):
    nome = models.CharField("Nome",max_length=100)
    sobrenome = models.CharField("sobrenome",max_length=100)
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'