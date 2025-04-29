
from rest_framework import serializers

from productos.serializers import ProductoSerializer
from .models import Carrito
from productos.models import Producto


class CarritoSerializer(serializers.ModelSerializer):
    producto_id = serializers.PrimaryKeyRelatedField(
        source='producto',
        queryset=Producto.objects.all(),
        write_only=True,  # Solo para hacer POST
    )

    producto = ProductoSerializer(read_only=True)  # Anida el producto completo

    class Meta:
        model = Carrito
        #fields = '__all__'
        fields = ['id', 'producto_id', 'producto', 'cantidad', 'fecha_agregado']