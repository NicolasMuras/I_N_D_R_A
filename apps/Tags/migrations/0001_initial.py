# Generated by Django 3.1.7 on 2021-04-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('colour', models.CharField(max_length=200, verbose_name='Color')),
                ('hour', models.CharField(max_length=200, verbose_name='Hora')),
                ('day', models.CharField(max_length=200, verbose_name='Dia')),
                ('month', models.CharField(max_length=200, verbose_name='Mes')),
                ('year', models.CharField(max_length=200, verbose_name='Año')),
                ('priority', models.CharField(max_length=200, verbose_name='Prioridad')),
            ],
            options={
                'verbose_name': 'Tag',
            },
        ),
    ]