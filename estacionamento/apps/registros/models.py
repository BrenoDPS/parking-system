from django.db import models
from apps.veiculos.models import Veiculo

class RegistroEstacionamento(models.Model):
    STATUS_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    placa_reconhecida = models.CharField(max_length=8)
    data_registro = models.DateTimeField(auto_now_add=True)
    tempo_total_segundos = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-data_registro']
        verbose_name = 'Registro de Estacionamento'
        verbose_name_plural = 'Registros de Estacionamento'

    def __str__(self):
        return f"{self.placa_reconhecida} - {self.status} - {self.data_registro}"
    
