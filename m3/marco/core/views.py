from django.views.generic import FormView # se nao tiver formulario e so TemplateView
from .models import Servico, Funcionario
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    #aula 54
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()#esse order_by e pra odernar com base em algum parametro caso nao queiro usa so o objects.all()  
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context
    #esse dois metodo e pra envio de email
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request,"E-mail enviado com sucesso")
        return super(IndexView,self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        form.send_mail()
        messages.error(self.request,"Erro ao enviar e-mail")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
