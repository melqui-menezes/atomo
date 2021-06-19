from django.db import models
from ckeditor.fields import RichTextField

class SobreNos(models.Model):
	titulo = models.CharField(max_length=60)
	descricao = RichTextField()

class ServicoProduto(models.Model):
    icone = models.ImageField(upload_to='static/images')
    titulo = models.CharField(max_length=30)
    descricao = RichTextField()

class Perguntas(models.Model):
	pergunta = models.CharField(max_length=60)
	resposta = RichTextField()
