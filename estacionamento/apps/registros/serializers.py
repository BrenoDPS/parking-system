from rest_framework import serializers
from .models import RegistroEstacionamento
from apps.veiculos.serializers import VeiculoSerializer

class RegistroEstacionamentoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = RegistroEstacionamento
        fields = '__all__'
        read_only_fields = ['id', 'data_registro', 'tempo_total_segundos']

class RegistroDetalhadoSerializer(RegistroEstacionamentoSerializer):
    veiculo = VeiculoSerializer(read_only=True)
    
    class Meta(RegistroEstacionamentoSerializer.Meta):
        fields = '__all__'