# Generated by Django 3.2 on 2021-04-14 18:15

from django.db import migrations, models

import cadastro.utils


class Migration(migrations.Migration):

    dependencies = [
        ("cadastro", "0002_auto_20210414_1258"),
    ]

    operations = [
        migrations.AddField(
            model_name="contrato",
            name="dt_cadastro",
            field=models.DateField(
                auto_now_add=True, default="2021-04-14", verbose_name="Data de cadastro"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contrato",
            name="dt_modidicacao",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Última atualização"
            ),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="cpf",
            field=models.CharField(
                help_text="Somente números",
                max_length=11,
                unique=True,
                validators=[cadastro.utils.validate_cpf],
                verbose_name="CPF",
            ),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="dt_modificacao",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Última atualização"
            ),
        ),
        migrations.AlterField(
            model_name="empresa",
            name="dt_modificacao",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Última atualização"
            ),
        ),
        migrations.AlterField(
            model_name="sistema",
            name="dt_modidicacao",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Última atualização"
            ),
        ),
    ]
