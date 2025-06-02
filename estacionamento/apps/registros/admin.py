from django.contrib import admin
from .models import RegistroEstacionamento

@admin.register(RegistroEstacionamento)
class RegistroEstacionamentoAdmin(admin.ModelAdmin):
    list_display = ('placa_reconhecida', 'status', 'veiculo', 'data_registro',
                    'tempo_total_segundos')
    list_filter = ('status', 'veiculo')
    search_fields = ('placa_reconhecida', 'veiculo_placa')
    readonly_fields = ('data_registro', 'tempo_total_segundos')
    autocomplete_fields = ['veiculo',]

    fieldsets = (
        (None, {
            'fields': (
                'placa_reconhecida', 'status', 'veiculo'
            )
        }),
        ('Informações de tempo', {
            'fields': ('data_registro', 'tempo_total_segundos')
        }),
    )