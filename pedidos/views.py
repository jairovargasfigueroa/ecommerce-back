from core.viewsets import BaseViewSet
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.permissions import IsAuthenticated

class PedidoViewSet(BaseViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    basename = 'pedidos'
    filter_by_user = True  # Cliente verá solo sus pedidos
    #permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     # Solo muestra los pedidos del usuario logueado
    #     return Pedido.objects.filter(usuario=self.request.user)