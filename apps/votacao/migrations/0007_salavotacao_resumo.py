# Generated by Django 3.2.7 on 2021-09-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0006_auto_20210916_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='salavotacao',
            name='resumo',
            field=models.CharField(default=1, max_length=30, verbose_name='Resumo'),
            preserve_default=False,
        ),
    ]