from django.shortcuts import render
from core.viewsets import BaseViewSet
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import AllowAny
from core.permissions import PermisoPorRol

class ProductoViewSet(BaseViewSet):
    queryset = Producto.objects.all()  # Obtiene todos los productos
    serializer_class = ProductoSerializer  # Utiliza el serializador definido
    basename = 'productos'
    
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]  # Permitir ver productos sin login
        return [PermisoPorRol()]

# Create your views here.
