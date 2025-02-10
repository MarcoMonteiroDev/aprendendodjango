from django.shortcuts import render, redirect
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto

def index(request):
    context = {
        "produtos": Produto.objects.all()
    }
    return render(request, "index.html", context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST': #como a funçao faz tanto post como get tem que verificar
        if form.is_valid():
            form.send_mail()
            messages.success(request, "E-mail Enviado com sucesso")
            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar E-mail")

    context = {
        'form': form
    }

    return render(request,"contato.html", context)

def produto(request):
    if str(request.user) != "AnonymousUser":
        if str(request.method) == "POST":
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                """
                prod = form.save(commit=False)
                print(f"Nome{prod.nome}")
                print(f"Preço{prod.preco}")
                print(f"Estoque{prod.estoque}")
                print(f"Imagem{prod.imagem}") """

                form.save()

                messages.success(request, "Produto salvo com sucesso")
                form = ProdutoModelForm()
            else:
                messages.error(request, "Erro ao salvar produto")
        else:
            form = ProdutoModelForm()
        context = {
            "form": form
        }
    else:
        return redirect("index")

    return render(request,"produto.html",context)
