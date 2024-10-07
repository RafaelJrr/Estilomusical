# Generated by Django 5.1.1 on 2024-09-17 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estilos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estilos', models.ForeignKey(default='SP', on_delete=django.db.models.deletion.CASCADE, to='estilos.estilo')),
            ],
        ),
    ]