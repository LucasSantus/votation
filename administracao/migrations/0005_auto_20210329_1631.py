# Generated by Django 3.0.13 on 2021-03-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0004_auto_20210324_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa_voto',
            name='quantidade_votos',
            field=models.IntegerField(null=True, verbose_name='Quantidade de Votos'),
        ),
    ]