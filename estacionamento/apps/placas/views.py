from rest_framework import permissions, viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PlacaDetectada
from .serializers import PlacaDetectadaSerializer


class PlacaDetectadaCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # data = {'placa': request.data.get('placa')}
        serializer = PlacaDetectadaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlacaDetectadaViewSet(mixins.RetrieveModelMixin, 
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = PlacaDetectada.objects.all()
    serializer_class = PlacaDetectadaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


"""
@csrf_exempt
def placas_list(request):
    
    # View para listar placas com filtros e paginação
    
    try:
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        collection = db[settings.MONGODB_COLLECTION]

        placa = request.GET.get('placa')
        tipo_evento = request.GET.get('tipo_evento')
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')
        limit = int(request.GET.get('limit', 10))
        page = int(request.GET.get('page', 1))

        # Query base
        query = {}
        if placa:
            query['placa'] = placa
        if tipo_evento:
            query['tipo_evento'] = tipo_evento
        if data_inicio:
            query['data_hora'] = {'$gte': datetime.fromisoformat(data_inicio)}
        if data_fim:
            query['data_hora'] = {'$lte': datetime.fromisoformat(data_fim)}

        # Buscar documentos
        cursor = collection.find(query).sort('data_hora', -1)
        total = collection.count_documents(query)

        # Paginação
        skip = (page - 1) * limit
        cursor = cursor.skip(skip).limit(limit)
        # Preparar resposta
        placas_data = [{
            'placa': doc['placa'],
            'data_hora': doc['data_hora'].isoformat() if isinstance(doc['data_hora'], datetime) else doc['data_hora'],
            'tipo_evento': doc['tipo_evento'],
            'tempo_total': doc.get('tempo_total_segundos'),
            'id': str(doc['_id'])
        } for doc in cursor]

        return JsonResponse({
            'status': 'success',
            'data': placas_data,
            'pagination': {
                'total': total,
                'pages': (total + limit - 1) // limit,
                'current_page': page,
                'has_next': (page * limit) < total,
                'has_previous': page > 1
            }
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
    finally:
        client.close()

@csrf_exempt
def placa_detail(request, placa):
    
    # View para detalhes de uma placa específica
    
    try:
        # Buscar todos os registros da placa
        registros = Placa.objects.filter(placa=placa).order_by('-data_hora')
        
        if not registros:
            return JsonResponse({
                'status': 'error',
                'message': 'Placa não encontrada'
            }, status=404)

        # Calcular estatísticas
        total_registros = registros.count()
        entradas = registros.filter(tipo_evento='entrada').count()
        saidas = registros.filter(tipo_evento='saida').count()
        
        # Calcular tempo médio de permanência
        tempos = [r.tempo_total_segundos for r in registros if r.tempo_total_segundos]
        tempo_medio = sum(tempos) / len(tempos) if tempos else 0

        # Preparar histórico
        historico = [{
            'data_hora': r.data_hora.isoformat(),
            'tipo_evento': r.tipo_evento,
            'tempo_total': r.tempo_total_segundos,
            'id': str(r.id)
        } for r in registros]

        return JsonResponse({
            'status': 'success',
            'placa': placa,
            'estatisticas': {
                'total_registros': total_registros,
                'entradas': entradas,
                'saidas': saidas,
                'tempo_medio_segundos': round(tempo_medio, 2)
            },
            'historico': historico
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@csrf_exempt
def placas_statistics(request):
    
    # View para estatísticas gerais das placas
    
    try:
        # Parâmetros de filtro
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')

        # Query base
        query = Placa.objects.all()

        # Aplicar filtros de data
        if data_inicio:
            query = query.filter(data_hora__gte=datetime.fromisoformat(data_inicio))
        if data_fim:
            query = query.filter(data_hora__lte=datetime.fromisoformat(data_fim))

        # Estatísticas gerais
        total_placas = query.distinct('placa').count()
        total_registros = query.count()
        total_entradas = query.filter(tipo_evento='entrada').count()
        total_saidas = query.filter(tipo_evento='saida').count()

        # Tempo médio de permanência
        tempos = [r.tempo_total_segundos for r in query if r.tempo_total_segundos]
        tempo_medio = sum(tempos) / len(tempos) if tempos else 0

        # Placas mais frequentes
        placas_frequentes = query.aggregate([
            {'$group': {'_id': '$placa', 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}},
            {'$limit': 5}
        ])

        return JsonResponse({
            'status': 'success',
            'estatisticas': {
                'total_placas_unicas': total_placas,
                'total_registros': total_registros,
                'total_entradas': total_entradas,
                'total_saidas': total_saidas,
                'tempo_medio_segundos': round(tempo_medio, 2),
                'placas_mais_frequentes': list(placas_frequentes)
            }
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
    

@csrf_exempt
def placas_nao_associadas(request):
    
    # View para listar placas detectadas que não têm veículo associado
    
    try:
        # Buscar placas não associadas usando o novo campo veiculo_associado
        placas = Placa.objects.filter(veiculo_associado=False).distinct('placa')
        
        resultado = []
        for placa in placas:
            registros = Placa.objects.filter(placa=placa).order_by('-data_hora')
            ultimo_registro = registros.first()
            
            resultado.append({
                'placa': placa,
                'ultima_deteccao': ultimo_registro.data_hora.isoformat(),
                'total_registros': registros.count(),
                'registro_id': str(ultimo_registro.id)
            })
        
        return JsonResponse({
            'status': 'success',
            'placas': resultado
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
        """