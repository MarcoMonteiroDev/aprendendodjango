from django.db import models
from stdimage.models import StdImageField
#SIGNALS sever para mandar um sinal para que antes ou depois de colocar algo no banco de dados fazer algo
from django.db.models import signals
#SLUG pega um nome ou um titulo para fazer uma url vailida
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField("Data da Criação", auto_now_add=True)
    modificado = models.DateField("Data de Atualização", auto_now=True)
    ativo = models.BooleanField("ativo?", default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    estoque = models.IntegerField("Estoque")
    imagem = StdImageField("Imagem", upload_to="produtos", variations={"themb":(124, 124)}) #aqui ele cria uma imagem com esse tamanho
    slug = models.SlugField("Slug",max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)