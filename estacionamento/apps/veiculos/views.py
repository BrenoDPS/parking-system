from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Veiculo
from .serializers import VeiculoSerializer, VeiculoDetalhadoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.select_related('usuario').all()
    serializer_class = VeiculoSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VeiculoDetalhadoSerializer
        return VeiculoSerializer
    
    def get_queryset(self):
        queryset = Veiculo.objects.select_related('usuario').all()
        
        # Filtros
        marca = self.request.query_params.get('marca')
        usuario_id = self.request.query_params.get('usuario')
        
        if marca:
            queryset = queryset.filter(marca__icontains=marca)
        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
            
        return queryset.order_by('-data_cadastro')
    
    @action(detail=False, methods=['get'])
    def buscar_por_placa(self, request):
        """Busca veículo por placa"""
        placa = request.query_params.get('placa', '').upper()
        if placa:
            try:
                veiculo = Veiculo.objects.select_related('usuario').get(placa=placa)
                serializer = VeiculoDetalhadoSerializer(veiculo)
                return Response(serializer.data)
            except Veiculo.DoesNotExist:
                return Response(
                    {'error': 'Veículo não encontrado'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response({'error': 'Placa é obrigatória'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def por_usuario(self, request):
        """Lista veículos de um usuário"""
        usuario_id = request.query_params.get('usuario_id')
        if usuario_id:
            veiculos = Veiculo.objects.filter(usuario_id=usuario_id)
            serializer = self.get_serializer(veiculos, many=True)
            return Response(serializer.data)
        return Response({'error': 'ID do usuário é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def historico(self, request, pk=None):
        """Histórico de registros de um veículo"""
        veiculo = self.get_object()
        from apps.registros.serializers import RegistroEstacionamentoSerializer
        registros = veiculo.registroestacionamento_set.all().order_by('-data_registro')
        serializer = RegistroEstacionamentoSerializer(registros, many=True)
        return Response(serializer.data)