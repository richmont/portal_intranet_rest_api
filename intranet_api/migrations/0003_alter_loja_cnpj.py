# Generated by Django 5.1.5 on 2025-02-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet_api', '0002_alter_loja_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='cnpj',
            field=models.CharField(max_length=14),
        ),
    ]
