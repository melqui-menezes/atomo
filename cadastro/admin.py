import os

from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django_object_actions import DjangoObjectActions
from weasyprint import HTML

from .models import Cliente, Contrato, Empresa, Sistema


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ["nome", "sobrenome", "cpf", "email", "dt_cadastro", "ativo"]


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        "razao_social",
        "nome_fantasia",
        "contratante",
        "cnpj",
        "dt_cadastro",
        "dt_modificacao",
        "ativo",
    ]


@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = ["sistema", "dt_cadastro", "dt_modidicacao", "ativo"]


@admin.register(Contrato)
class ContratoAdmin(DjangoObjectActions, admin.ModelAdmin):

    exclude = ("dt_fim", "anuidade", "nm_contrato", "contrato_pdf")
    search_fields = ["contratante,"]
    list_display = [
        "contratante",
        "contrato_pdf",
        "sistema",
        "dt_inicio",
        "dt_fim",
        "anuidade",
        "ativo",
    ]

    def generate_pdf(self, request, obj):
        # import pdb; pdb.set_trace()
        html_string = render_to_string("contrato/pdf_template.html", {"obj": obj})
        html = HTML(string=html_string)
        html.write_pdf(target=f"media/contratos/{obj}.pdf")

        fs = FileSystemStorage(f"media/contratos/")

        with fs.open(f"{obj}.pdf") as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="{obj}.pdf"'
            Contrato.objects.filter(id=obj.id).update(
                contrato_pdf=f"contratos/{obj}.pdf"
            )
            return response

    generate_pdf.label = "Gerar PDF"
    generate_pdf.short_description = "Clique para gerar o PDF desse contrato"

    change_actions = ("generate_pdf",)
