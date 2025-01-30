from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST': #como a funçao faz tanto post como get tem que verificar
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print("Mensagem Enviada")
            print(f"Nome:{nome}")
            print(f"E-mail:{email}")
            print(f"Assunto:{assunto}")
            print(f"Mensagem:{mensagem}")

            messages.success(request, "E-mail Enviado com sucesso")
            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar E-mail")

    context = {
        'form': form
    }

    return render(request,"contato.html", context)

def produto(request):
    return render(request,"produto.html")
