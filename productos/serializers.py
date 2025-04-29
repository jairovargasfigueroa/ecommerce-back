from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'  # Incluye todos los campos del modelo Producto
        extra_kwargs = {
            'imagen': {'required': False},
            'nombre_categoria': {'required': True}
        }