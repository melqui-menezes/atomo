from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ClienteForm
from .models import Cliente, Contrato, Empresa, Sistema


class LoginView(TemplateView):
    template_name = "login.html"


class IndexView(TemplateView):
    template_name = "index.html"


class ClienteView(ListView):
    models = Cliente
    template_name = "clientes.html"
    queryset = Cliente.objects.all()
    context_object_name = "clientes"


class ClienteCadastroView(CreateView):
    models = Cliente
    template_name = "cadastro_cliente.html"
    queryset = Cliente.objects.all()
    fields = [
        "ativo",
        "cpf",
        "nome",
        "sobrenome",
        "contato_1",
        "contato_2",
        "email",
        "rua",
        "num_casa",
        "bairro",
        "cidade",
        "estado",
        "cep",
    ]
    success_url = reverse_lazy("clientes")


class ClienteUpdateView(UpdateView):
    models = Cliente
    template_name = "cadastro_cliente.html"
    queryset = Cliente.objects.all()
    fields = [
        "ativo",
        "cpf",
        "nome",
        "sobrenome",
        "contato_1",
        "contato_2",
        "email",
        "rua",
        "num_casa",
        "bairro",
        "cidade",
        "estado",
        "cep",
    ]
    success_url = reverse_lazy("clientes")


class ClienteDeleteView(DeleteView):
    models = Cliente
    template_name = "cliente_del.html"
    queryset = Cliente.objects.all()
    success_url = reverse_lazy("clientes")
