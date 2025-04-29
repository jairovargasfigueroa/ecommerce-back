from django.shortcuts import render

from core.pagination import CustomPagination
from core.viewsets import BaseViewSet
from .filters import ProductoFilter
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import AllowAny
from core.permissions import PermisoPorRol
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ProductoViewSet(BaseViewSet):
    queryset = Producto.objects.all()  # Obtiene todos los productos
    serializer_class = ProductoSerializer  # Utiliza el serializador definido
    basename = 'productos'

    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']  # Campos donde quieres buscar
    filterset_class = ProductoFilter
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]  # Permitir ver productos sin login
        return [PermisoPorRol()]

# Create your views here.
