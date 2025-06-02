from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import RegistroEstacionamento
from .serializers import RegistroEstacionamentoSerializer
from .services import ControleAcessoService
from apps.placas.models import PlacaDetectada
from apps.veiculos.models import Veiculo

class RegistroEstacionamentoViewSet(viewsets.ModelViewSet):
    queryset = RegistroEstacionamento.objects.all()
    serializer_class = RegistroEstacionamentoSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Permite criar um registro de estacionamento a partir de uma placa detectada.
        Se 'placa_detectada' for informado, busca os dados da placa e do veículo automaticamente.
        """
        placa_id = request.data.get('placa_detectada')
        if placa_id:
            try:
                placa = PlacaDetectada.objects.get(id=placa_id)
                veiculo = placa.veiculo or Veiculo.objects.filter(placa=placa.placa).first()
                if not veiculo:
                    return Response({'error': 'Veículo não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
                tempo_total = None
                # Se for saída, calcula o tempo de permanência
                if placa.status == 'saida':
                    ultimo_registro = RegistroEstacionamento.objects.filter(
                        veiculo=veiculo, status='entrada'
                    ).order_by('-data_registro').first()
                    if ultimo_registro:
                        tempo_total = (placa.data_hora - ultimo_registro.data_registro).total_seconds()
                registro = RegistroEstacionamento.objects.create(
                    veiculo=veiculo,
                    status=placa.status,
                    placa_reconhecida=placa.placa,
                    data_registro=placa.data_hora,
                    tempo_total_segundos=tempo_total
                )
                placa.registro = registro
                placa.save()
                serializer = self.get_serializer(registro)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except PlacaDetectada.DoesNotExist:
                return Response({'error': 'Placa detectada não encontrada.'}, status=status.HTTP_400_BAD_REQUEST)
        # Caso não seja informado placa_detectada, segue o fluxo padrão do DRF
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    def hoje(self, request):
        """Registros de hoje"""
        hoje = timezone.now().date()
        registros = RegistroEstacionamento.objects.filter(
            data_registro_date=hoje
        ).select_related('veiculo', 'veiculo_usuario')
        
        serializer = self.get_serializer(registros, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def estatisticas_diarias(self, request):
        """Estatísticas do dia"""
        stats = ControleAcessoService.obter_estatisticas_diarias()
        return Response(stats)
    
    @action(detail=False, methods=['get'])
    def veiculos_no_estacionamento(self, request):
        """Veículos atualmente no estacionamento"""
        veiculos = ControleAcessoService.obter_veiculos_no_estacionamento()
        return Response(veiculos)
