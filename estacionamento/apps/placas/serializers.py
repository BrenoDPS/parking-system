from rest_framework import serializers
from .models import PlacaDetectada

class PlacaDetectadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaDetectada
        fields = ['id', 'placa', 'data_hora', 'status', 'veiculo', 'registro']
        read_only_fields = ['id']