from django.shortcuts import render
from rest_framework import parsers, filters

from core.viewsets import BaseViewSet
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import AllowAny
from core.permissions import PermisoPorRol

class ProductoViewSet(BaseViewSet):
    serializer_class = ProductoSerializer  # Utiliza el serializador definido
    basename = 'productos'
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'descripcion']

    def get_queryset(self):
        queryset = Producto.objects.all().order_by('-fecha_creacion')

        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)

        return queryset

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]  # Permitir ver productos sin login
        return [PermisoPorRol()]

# Create your views here.
