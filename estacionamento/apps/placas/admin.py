from django.contrib import admin
from django.http import HttpRequest
from .models import PlacaDetectada

class PlacaDetectadaAdmin(admin.ModelAdmin):
    readonly_fields = ('placa', 'data_hora')
    def has_add_permission(self, request):
        return False
    

admin.site.register(PlacaDetectada, PlacaDetectadaAdmin)
