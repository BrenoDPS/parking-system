from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q, Count
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_queryset(self):
        """Permite filtros via query params"""
        queryset = Usuario.objects.all()
        tipo = self.request.query_params.get('tipo')
        
        if tipo:
            queryset = queryset.filter(tipo_usuario=tipo)
            
        return queryset.order_by('-data_cadastro')
    
    @action(detail=False, methods=['get'])
    def por_tipo(self, request):
        """Lista usuários por tipo (aluno/funcionario)"""
        tipo = request.query_params.get('tipo')
        if tipo:
            usuarios = Usuario.objects.filter(tipo_usuario=tipo)
            serializer = self.get_serializer(usuarios, many=True)
            return Response(serializer.data)
        return Response({'error': 'Tipo não especificado'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def buscar(self, request):
        """Busca usuários por nome, matrícula ou email"""
        q = request.query_params.get('q', '')
        if q:
            usuarios = Usuario.objects.filter(
                Q(nome__icontains=q) |
                Q(matricula__icontains=q) |
                Q(email__icontains=q)
            )
            serializer = self.get_serializer(usuarios, many=True)
            return Response(serializer.data)
        return Response([])
    
    @action(detail=False, methods=['get'])
    def estatisticas(self, request):
        """Estatísticas de usuários"""
        total = Usuario.objects.count()
        por_tipo = Usuario.objects.values('tipo_usuario').annotate(count=Count('id'))
        
        return Response({
            'total_usuarios': total,
            'por_tipo': {item['tipo_usuario']: item['count'] for item in por_tipo}
        })
    
    @action(detail=True, methods=['get'])
    def veiculos(self, request, pk=None):
        """Lista veículos de um usuário específico"""
        usuario = self.get_object()
        from apps.veiculos.serializers import VeiculoSerializer
        veiculos = usuario.veiculo_set.all()
        serializer = VeiculoSerializer(veiculos, many=True)
        return Response(serializer.data)