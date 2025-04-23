from rest_framework import serializers
from productos.models import Producto
from .models import ItemPedido, Pedido


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['id', 'pedido', 'producto', 'cantidad', 'precio_unitario']
        read_only_fields = ['pedido'] 
        extra_kwargs = {
            'producto': {'required': True},
            'cantidad': {'required': True},
            'precio_unitario': {'required': True},
        }


class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True)
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'monto_total', 'tipo_pago', 'tipo_entrega', 'estado', 'fecha_pedido', 'items']
        read_only_fields = ['fecha_pedido', 'usuario', 'monto_total']

    def create(self, validated_data):
        request = self.context.get('request')
        usuario = request.user if request else None  
        items_data = validated_data.pop('items')
        estado = validated_data.pop('estado')
        tipo_pago = validated_data.pop('tipo_pago')
        tipo_entrega = validated_data.pop('tipo_entrega')
        monto_total = 0

        # Crear pedido vacío
        pedido = Pedido.objects.create(
            usuario=usuario,
            monto_total=0,
            estado=estado,
            tipo_pago=tipo_pago,
            tipo_entrega=tipo_entrega
        )

        for item in items_data:
            producto = Producto.objects.get(nombre=item['producto'])
            cantidad = int(item['cantidad'])
            precio_unitario = float(item['precio_unitario'])

            ItemPedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )
            monto_total += cantidad * precio_unitario

        pedido.monto_total = monto_total
        pedido.save()
        return pedido
    
    def update(self, instance, validated_data):
    # Solo permitimos modificar el estado del pedido
        # estado = validated_data.get('estado', instance.estado)
        # instance.estado = estado
        instance.tipo_entrega = validated_data.get('tipo_entrega', instance.tipo_entrega)
        instance.tipo_pago = validated_data.get('tipo_pago', instance.tipo_pago)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.save()
        return instance

