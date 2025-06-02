from rest_framework import serializers
from .models import Veiculo
from apps.usuarios.serializers import UsuarioSerializer

class VeiculoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)
    usuario_matricula = serializers.CharField(source='usuario.matricula', read_only=True)
    
    class Meta:
        model = Veiculo
        fields = '__all__'
        read_only_fields = ('data_cadastro',)
    
    def validate_placa(self, value):
        # Validação simples de placa brasileira
        if len(value) < 7 or len(value) > 8:
            raise serializers.ValidationError("Placa deve ter entre 7 e 8 caracteres")
        return value.upper()

class VeiculoDetalhadoSerializer(VeiculoSerializer):
    usuario = UsuarioSerializer(read_only=True)
    
    class Meta(VeiculoSerializer.Meta):
        fields = '__all__'