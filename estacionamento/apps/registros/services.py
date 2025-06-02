from django.utils import timezone
from .models import RegistroEstacionamento
from apps.veiculos.models import Veiculo
from apps.placas.models import PlacaDetectada
from django.db import transaction

class ControleAcessoService:
    @staticmethod
    def registrar_movimento(placa, status, data_hora):
        try:
            # Busca o veículo no PostgreSQL
            veiculo = Veiculo.objects.get(placa=placa)
            tempo_total = None

            if status == 'saida':
                ultimo_registro = RegistroEstacionamento.objects.filter(
                    veiculo=veiculo, status='entrada'
                ).order_by('-data_registro').first()
                if ultimo_registro:
                    tempo_total = (data_hora - ultimo_registro.data_registro
                    ).total_seconds()

            novo_registro = RegistroEstacionamento.objects.create(
                veiculo=veiculo,
                status=status,
                placa_reconhecida=placa,
                data_registro=data_hora,
                tempo_total_segundos=tempo_total
            )

            placa_detectada = PlacaDetectada.objects.filter(
                placa=placa, data_hora=data_hora
            ).first()
            if placa_detectada:
                placa_detectada.registro = novo_registro
                placa_detectada.veiculo = veiculo
                placa_detectada.save()

            return {
                'success': True,
                'status': status,
                'registro': novo_registro,
                'tempo_total': tempo_total
            }
        except Veiculo.DoesNotExist:
            return {
                'success': False,
                'error': 'Veiculo inexistente no sistema',
                'placa': placa
            }
        except Exception as e:
            return {
            'success': False,
            'error': f'Erro ao processar registro: {str(e)}',
            'placa': placa
        }
            

    @staticmethod
    def obter_estatisticas_diarias():
        hoje = timezone.now().date()
        registros = RegistroEstacionamento.objects.filter(
            data_registro_date=hoje
        )

        total_entradas = registros.filter(status='entrada').count()
        total_saidas = registros.filter(status='saida').count()
        veiculos_presentes = total_entradas - total_saidas

        return {
            'data': hoje,
            'total_entradas': total_entradas,
            'total_saidas': total_saidas,
            'veiculos_presentes': veiculos_presentes
        }

    @staticmethod
    def obter_veiculos_no_estacionamento():
        veiculos_presentes = []
        veiculos = Veiculo.objects.all()

        for veiculo in veiculos:
            ultimo_registro = RegistroEstacionamento.objects.filter(
                veiculo=veiculo
            ).order_by('-data_registro').first()

            if ultimo_registro and ultimo_registro.status == 'entrada':
                veiculos_presentes.append({
                    'placa': veiculo.placa,
                    'usuario': veiculo.usuario.nome,
                    'entrada': ultimo_registro.data_registro,
                    'tempo_permanencia': ultimo_registro.tempo_total_segundos
                })

        return veiculos_presentes
