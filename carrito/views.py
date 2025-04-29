from rest_framework import viewsets

from core.viewsets import BaseViewSet
from .models import Carrito
from .serializers import CarritoSerializer

class CarritoViewSet(BaseViewSet):
    queryset = Carrito.objects.all()  # Obtiene todos los productos
    serializer_class = CarritoSerializer  # Utiliza el serializador definido
    basename = 'carritos'
    filter_by_user = True

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
