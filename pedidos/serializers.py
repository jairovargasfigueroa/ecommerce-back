from rest_framework import serializers
from .models import ItemPedido, Pedido


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = [ 'id', 'pedido', 'producto', 'cantidad', 'precio_unitario']

class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pedido
        fields = [  'id', 'monto_total', 'estado', 'fecha_pedido', 'items']
        read_only_fields = ['estado', 'fecha_pedido']        
        
    def create(self , validated_data):
        items_data = validated_data.pop('items')    
        pedido = Pedido.objects.create(**validated_data)

        for item_data in items_data:
            # Verificar si el producto ya existe en el pedido
            producto = item_data['producto']
            # Si el producto ya está en el pedido, actualizamos la cantidad
            existing_item = ItemPedido.objects.filter(pedido=pedido, producto=producto).first()

            if existing_item:
                # Si ya existe, sumamos la cantidad al item existente
                existing_item.cantidad += item_data['cantidad']
                existing_item.save()
            else:
                # Si no existe, creamos un nuevo item
                ItemPedido.objects.create(pedido=pedido, **item_data)

        return pedido