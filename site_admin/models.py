from ckeditor.fields import RichTextField
from django.db import models


class SobreNos(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = RichTextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Sobre Nós"


class ServicoProduto(models.Model):
    icone = models.ImageField(upload_to="static/images")
    titulo = models.CharField(max_length=30)
    descricao = RichTextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Serviços e Produtos"


class Perguntas(models.Model):
    pergunta = models.CharField(max_length=60)
    resposta = RichTextField()

    def __str__(self):
        return self.pergunta

    class Meta:
        verbose_name_plural = "Perguntas Frequentes"
