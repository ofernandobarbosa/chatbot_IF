# Generated by Django 4.0.6 on 2022-07-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_calendario_categoria_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='categoria_evento',
            field=models.IntegerField(choices=[(1, 'Período Letivo'), (2, 'Feriados'), (3, 'Notícias'), (4, 'Processo Seletivo'), (5, 'Benefícios Estudantis'), (6, 'Cursos Ofertados'), (7, 'EAD'), (8, 'Informações de Servidores'), (9, 'Informações do IFRS')]),
        ),
    ]