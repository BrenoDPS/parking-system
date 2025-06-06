# Generated by Django 5.2.1 on 2025-05-23 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('veiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroEstacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída')], max_length=20)),
                ('placa_reconhecida', models.CharField(max_length=8)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.veiculo')),
            ],
        ),
    ]
