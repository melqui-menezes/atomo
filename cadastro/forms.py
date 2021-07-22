from django.contrib.auth.forms import forms

from cadastro.models import Cliente, Contrato, Empresa, Sistema


class ClienteForm(forms.Form):
    class Meta:
        model = Cliente
        fields = "__all__"

        widgets = {
            "cpf": forms.TextInput(attrs={"data-field-mask": "000.000.000-00"}),
            "contato_1": forms.TextInput(attrs={"data-field-mask": "(00)00000-0000)"}),
            "contato_2": forms.TextInput(attrs={"data-field-mask": "(00)00000-0000)"}),
            "cep": forms.TextInput(attrs={"data-field-mask": "00000-000"}),
        }
