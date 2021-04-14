from django.core.exceptions import ValidationError
import re

def validate_cpf(cpf):

    cpf = re.sub(r"\W", "", cpf)
    if re.match(r"(\d)\1{10}", cpf) or len(cpf) != 11:
        raise ValidationError(
            ('Por favor, insira um CPF válido'),
            params={'cpf': cpf},
            )
    d1, d2, i = 0, 0, 0
    while i < 10:
        d1, d2, i = (
            (d1 + (int(cpf[i]) * (11 - i - 1))) % 11 if i < 9 else d1,
            (d2 + (int(cpf[i]) * (11 - i))) % 11,
            i + 1,
        )
    return (int(cpf[9]) == (11 - d1 if d1 > 1 else 0)) and (
        int(cpf[10]) == (11 - d2 if d2 > 1 else 0)
    )

def select_state():
    states = (
        ("AC","Acre"),
        ("AL","Alagoas"),
        ("AP","Amapá"),
        ("AM","Amazonas"),
        ("BA","Bahia"),
        ("CE","Ceará"),
        ("DF","Distrito Federal"),
        ("ES","Espírito Santo"),
        ("GO","Goiás"),
        ("MA","Maranhão"),
        ("MT","Mato Grosso"),
        ("MS","Mato Grosso do Sul"),
        ("MG","Minas Gerais"),
        ("PA","Pará"),
        ("PB","Paraíba"),
        ("PR","Paraná"),
        ("PE","Pernambuco"),
        ("PI","Piauí"),
        ("RR","Roraima"),
        ("RO","Rondônia"),
        ("RJ","Rio de Janeiro"),
        ("RN","Rio Grande do Norte"),
        ("RS","Rio Grande do Sul"),
        ("SC","Santa Catarina"),
        ("SP","São Paulo"),
        ("SE","Sergipe"),
        ("TO","Tocantins")
    )
    return states