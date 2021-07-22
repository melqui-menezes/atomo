# Generated by Django 3.2 on 2021-07-22 15:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Perguntas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pergunta", models.CharField(max_length=60)),
                ("resposta", ckeditor.fields.RichTextField()),
            ],
            options={
                "verbose_name_plural": "Perguntas Frequentes",
            },
        ),
        migrations.CreateModel(
            name="ServicoProduto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("icone", models.ImageField(upload_to="static/images")),
                ("titulo", models.CharField(max_length=30)),
                ("descricao", ckeditor.fields.RichTextField()),
            ],
            options={
                "verbose_name_plural": "Serviços e Produtos",
            },
        ),
        migrations.CreateModel(
            name="SobreNos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=60)),
                ("descricao", ckeditor.fields.RichTextField()),
            ],
            options={
                "verbose_name_plural": "Sobre Nós",
            },
        ),
    ]
