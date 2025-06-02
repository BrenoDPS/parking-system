from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'cor', 'usuario', 'data_cadastro')
    list_filter = ('marca', 'cor', 'data_cadastro')
    search_fields = ('placa', 'marca', 'modelo', 'usuario__nome')
    readonly_fields = ('data_cadastro',)
