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
            ItemPedido.objects.create(pedido=pedido, **item_data)
            
        return pedido    