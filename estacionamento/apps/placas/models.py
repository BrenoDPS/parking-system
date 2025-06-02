from django.db import models
from datetime import datetime


class PlacaDetectada(models.Model):
    STATUS_EVENTO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]
    placa = models.CharField(max_length=8)
    data_hora = models.DateTimeField(default=datetime.now)
    status = models.CharField(
        max_length=10,
        choices=STATUS_EVENTO,
    )
    veiculo = models.ForeignKey(
        'veiculos.Veiculo',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    registro = models.ForeignKey(
        'registros.RegistroEstacionamento',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    meta = {
        'collection': 'placas_detectadas',
        'db_alias': 'default',
        'indexes': [
            ('placa', '-data_hora'),
            ('tipo_evento', '-data_hora'),
            ('data_hora',)
        ]
    }

    class Meta:
        ordering = ['-data_hora']
        verbose_name = 'Placa Detectada'
        verbose_name_plural = 'Placas Detectadas'


    def __str__(self):
        return f"{self.placa} - {self.data_hora}"
    