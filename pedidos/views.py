from core.pagination import CustomPagination
from core.viewsets import BaseViewSet
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PedidoViewSet(BaseViewSet):
    queryset = Pedido.objects.all().order_by('-fecha_pedido')  # 👈 más reciente primero
    serializer_class = PedidoSerializer
    basename = 'pedidos'
    pagination_class = CustomPagination
    filter_by_user = True  # Para que el cliente solo vea sus propios pedidos


    def perform_create(self, serializer):
        # Asociar automáticamente el usuario autenticado
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=['get'], url_path='pendiente-actual')
    def pedido_pendiente_actual(self, request):
        pedido = Pedido.objects.filter(usuario=request.user, estado='pendiente').order_by('-fecha_pedido').first()
        if pedido:
            serializer = self.get_serializer(pedido)
            return Response(serializer.data)
        return Response({'detail': 'No hay pedidos pendientes'}, status=404)

