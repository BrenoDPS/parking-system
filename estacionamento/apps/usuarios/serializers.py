from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('data_cadastro',)

    def validate_matricula(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("A matrícula deve conter pelo menos 6 caracteres.")
        return value
