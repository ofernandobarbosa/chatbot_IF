# Generated by Django 4.0.6 on 2022-07-30 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_evento_data_de_fim_alter_evento_data_de_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='sobrenome_do_professor',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
