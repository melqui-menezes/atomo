from django.contrib import admin

from .models import Perguntas, ServicoProduto, SobreNos


@admin.register(SobreNos)
class SobreNosAdmin(admin.ModelAdmin):
    list_display = ["titulo", "descricao"]


@admin.register(ServicoProduto)
class ServicoProdutoAdmin(admin.ModelAdmin):
    list_display = ["icone", "titulo", "descricao"]


@admin.register(Perguntas)
class PerguntasAdmin(admin.ModelAdmin):
    list_display = ["pergunta", "resposta"]
