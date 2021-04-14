from django.contrib import admin

from .models import Cliente, Empresa, Sistema, Contrato


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 
        'sobrenome', 
        'cpf',
        'email',
        'dt_cadastro',
        'ativo'
    ]


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'razao_social', 
        'nome_fantasia',
        'contratante',
        'cnpj',
        'dt_cadastro', 
        'dt_modificacao',  
        'ativo'
    ]


@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = ['sistema','dt_cadastro','dt_modidicacao','ativo']


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):

    exclude = ('dt_fim','anuidade')

    list_display = [
        'contratante',
        'sistema',
        'dt_inicio',
        'dt_fim',
        'anuidade',
        'ativo'
    ]