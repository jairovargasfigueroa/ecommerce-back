from rest_framework import viewsets
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.permissions import IsAuthenticated

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo muestra los pedidos del usuario logueado
        return Pedido.objects.filter(usuario=self.request.user)