from core.pagination import CustomPagination
from core.viewsets import BaseViewSet
from notificaciones.fmc import enviar_notificacion_fcm
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PedidoViewSet(BaseViewSet):
    queryset = Pedido.objects.all().order_by('-fecha_pedido')  # 👈 más reciente primero
    serializer_class = PedidoSerializer
    basename = 'pedidos'
    pagination_class = CustomPagination 
    

    def perform_create(self, serializer):
        # Asociar automáticamente el usuario autenticado
        pedido = serializer.save(usuario=self.request.user)

        # Solo si el pedido es "pendiente" y el usuario tiene token
        if pedido.estado == 'pendiente' and pedido.usuario.fcm_token:
            try:
                enviar_notificacion_fcm(
                    token=pedido.usuario.fcm_token,
                    titulo="Pedido confirmado",
                    mensaje="Tu pedido fue recibido y está siendo procesado."
                )
            except Exception as e:
                print(f"Error al enviar notificación: {e}")

    def get_queryset(self):
        # Filtrar por usuario si no es admin
        if self.filter_by_user:
            return self.queryset.filter(usuario=self.request.user)
        return self.queryset

    @action(detail=False, methods=['get'], url_path='pendiente-actual')
    def pedido_pendiente_actual(self, request):
        pedido = Pedido.objects.filter(usuario=request.user, estado='pendiente').order_by('-fecha_pedido').first()
        if pedido:
            serializer = self.get_serializer(pedido)
            return Response(serializer.data)
        return Response({'detail': 'No hay pedidos pendientes'}, status=404)

        