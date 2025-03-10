from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    criado = models.DateField("Criação", auto_now_add=True)
    modificado = models.DateField("Modificado", auto_now=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog','Engrenagem'),
        ('lni-stats-up','Grafico'),
        ('lni-users','Usuarios'),
        ('lni-layers','Design'),
        ('lni-mobile','Mobile'),
        ('lni-rocket','Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField("descrição", max_length=200)
    icone = models.CharField("Icone", max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico