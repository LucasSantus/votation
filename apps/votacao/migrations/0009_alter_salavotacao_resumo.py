# Generated by Django 3.2.7 on 2021-09-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0008_alter_salavotacao_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salavotacao',
            name='resumo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Resumo'),
        ),
    ]