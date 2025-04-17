from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()  # Obtiene todos los productos
    serializer_class = ProductoSerializer  # Utiliza el serializador definido
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create your views here.
