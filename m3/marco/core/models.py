from django.db import models
import uuid
from stdimage.models import StdImageField

def get_file_path(__instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


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
    
class Cargo(Base):
    cargo = models.CharField("Cargo",max_length=50)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
    
    def __str__(self):
        return self.cargo
    
class Funcionario(Base):
    nome = models.CharField("nome", max_length=100)
    cargo = models.ForeignKey("core.Cargo",verbose_name='Cargo',on_delete=models.CASCADE)
    bio = models.TextField("Bio", max_length=200)
    imagem = StdImageField("Imagem",upload_to=get_file_path, variations={'thumb':{'width':480, "height":480, 'crop':True}})
    facebook = models.CharField("Facebook", max_length=100, default='#')
    twitter = models.CharField("Twitter", max_length=100, default='#')
    instagran = models.CharField("Instagran", max_length=100, default='#')

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
    
    def __str__(self):
        return self.nome
    