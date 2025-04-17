from rest_framework import viewsets
from .models import Carrito
from .serializers import CarritoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()  # Obtiene todos los productos
    serializer_class = CarritoSerializer  # Utiliza el serializador definido
# Create your views here.
