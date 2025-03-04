from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome")
    email = forms.EmailField(label="E-mail")
    assunto = forms.CharField(label="Assunto")
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

    def send_mail(self):
            nome = self.cleaned_data['nome']
            email = self.cleaned_data['email']
            assunto = self.cleaned_data['assunto']
            mensagem = self.cleaned_data['mensagem']

            conteudo = f"Nome: {nome}\n Email: {email}\n Assunto: {assunto}\n Mensagem:{mensagem}"

            mail = EmailMessage(
                  subject="E-mail enviado pelo sistema django2", #poderia colocar o assunto aqui
                  body=conteudo,
                  from_email="contato@seudominio.com.br",
                  to=["contato@seudominio.com.br"],
                  headers= {"Reply_to": email}
            )
            mail.send()

class ProdutoModelForm(forms.ModelForm):

      class Meta:
            model = Produto
            fields = ["nome", "preco", "estoque", "imagem"]