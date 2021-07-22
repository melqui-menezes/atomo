import uuid
from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models

from .utils import BR_STATES, VENCTO, contract_name, get_upload_path


class Cliente(models.Model):

    ativo = models.BooleanField("Ativo?", default=True)
    dt_cadastro = models.DateField("Data de cadastro", auto_now_add=True)
    dt_modificacao = models.DateTimeField("Última atualização", auto_now=True)
    cpf = models.CharField(
        "CPF", max_length=11, help_text="Somente números", unique=True
    )
    nome = models.CharField("Nome", max_length=35)
    sobrenome = models.CharField("Sobrenome", max_length=35)
    contato_1 = models.CharField("Celular", max_length=11)
    contato_2 = models.CharField("Telefone", max_length=11)
    email = models.EmailField("E-mail", unique=True)
    rua = models.CharField("Endereço", max_length=50)
    num_casa = models.CharField("Número", max_length=6)
    bairro = models.CharField("Bairro", max_length=50)
    cidade = models.CharField("Cidade", max_length=50)
    estado = models.CharField("Estado", max_length=2, choices=BR_STATES)
    cep = models.CharField("CEP", max_length=9)

    def __str__(self):
        return f"{self.nome} {self.sobrenome} | CPF: {self.cpf}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Empresa(models.Model):

    ativo = models.BooleanField("Ativo?", default=True)
    dt_cadastro = models.DateField("Data de cadastro", auto_now_add=True)
    dt_modificacao = models.DateTimeField("Última atualização", auto_now=True)
    cnpj = models.CharField(
        "CNPJ", max_length=14, help_text="Somente números", unique=True
    )
    sefaz = models.CharField(
        "SEFAZ", max_length=14, help_text="Somente números", unique=True, null=True
    )
    razao_social = models.CharField("Razão Social", max_length=50)
    nome_fantasia = models.CharField("Nome Fantasia", max_length=50)
    rua = models.CharField("Endereço", max_length=50)
    num_casa = models.CharField("Número", max_length=6)
    bairro = models.CharField("Bairro", max_length=50)
    cidade = models.CharField("Cidade", max_length=50)
    estado = models.CharField("Estado", max_length=2, choices=BR_STATES)
    cep = models.CharField("CEP", max_length=9)
    contratante = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        verbose_name="Contratante",
        related_name="cliente_empresa",
    )

    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


class Sistema(models.Model):

    ativo = models.BooleanField("Ativo?", default=True)
    sistema = models.CharField(
        "Sistema", max_length=30, help_text="Informe o nome do sistema", unique=True
    )
    descricao = models.TextField("Descrição do sistema")
    dt_cadastro = models.DateField("Data de cadastro", auto_now_add=True)
    dt_modidicacao = models.DateTimeField("Última atualização", auto_now=True)

    def __str__(self):
        return self.sistema

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"


class Contrato(models.Model):

    ativo = models.BooleanField("Ativo?", default=True)
    nm_contrato = models.CharField("Contrato", max_length=60)
    contrato_pdf = models.FileField(blank=True, null=True, upload_to="contratos")
    dt_cadastro = models.DateField("Data de cadastro", auto_now_add=True)
    dt_modidicacao = models.DateTimeField("Última atualização", auto_now=True)
    sistema = models.ForeignKey(
        Sistema,
        on_delete=models.DO_NOTHING,
        verbose_name="Sistema",
        related_name="sistema_contrato",
    )
    contratante = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name="Contratante",
        related_name="empresa_contrato",
    )
    dt_inicio = models.DateField("Início")
    dt_fim = models.DateField("Final")
    mensalidade = models.DecimalField(
        "Valor mensal",
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
    )
    anuidade = models.DecimalField("Valor Total", max_digits=7, decimal_places=2)
    dia_vencimento = models.CharField("Dia de vencimento", max_length=2, choices=VENCTO)
    observacoes = models.TextField("Observações", null=True, default="Sem observações")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.anuidade = self.mensalidade * 12
            self.dt_fim = self.dt_inicio + timedelta(days=365)
            self.nm_contrato = contract_name(self.contratante)
        super(Contrato, self).save()

    def __str__(self):
        return self.nm_contrato

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
