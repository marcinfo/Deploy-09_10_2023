# Generated by Django 4.2.4 on 2023-09-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencias',
            name='Cultura',
            field=models.CharField(choices=[], help_text='Qual plantação foi contaminada?', max_length=45),
        ),
        migrations.AlterField(
            model_name='ocorrencias',
            name='praga',
            field=models.CharField(choices=[], help_text='Selecione qual o tipo de praga esta contaminando.', max_length=40),
        ),
        migrations.AlterField(
            model_name='tb_registros',
            name='cultura',
            field=models.CharField(blank=True, choices=[], help_text='Qual plantação foi contaminada?', max_length=45, null=True, verbose_name='Cultura'),
        ),
        migrations.AlterField(
            model_name='tb_registros',
            name='praga',
            field=models.CharField(choices=[], help_text='Selecione qual o tipo de praga esta contaminando.', max_length=40),
        ),
    ]
