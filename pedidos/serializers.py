from rest_framework import serializers

from notificaciones.fmc import enviar_notificacion_fcm
from notificaciones.models import Notificacion
from productos.models import Producto
from sucursales.models import Sucursal
from usuarios.models import DireccionEnvio
from .models import ItemPedido, Pedido


class ItemPedidoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.SerializerMethodField()
    class Meta:
        model = ItemPedido
        fields = ['id', 'pedido', 'producto', 'producto_nombre','cantidad', 'precio_unitario']
        read_only_fields = ['pedido'] 
        extra_kwargs = {
            'producto': {'required': True},
            'cantidad': {'required': True},
            'precio_unitario': {'required': True},
        }

    def get_producto_nombre(self, obj):
        # Devuelve el nombre del producto basado en la relación
        return obj.producto.nombre  # Esto muestra el nombre del producto


class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True)
    usuario = serializers.StringRelatedField(read_only=True)
    direccion_envio_id = serializers.PrimaryKeyRelatedField(
        queryset=DireccionEnvio.objects.all(), source='direccion_envio', write_only=True, allow_null=True,
        required=False
    )
    sucursal_retiro_id = serializers.PrimaryKeyRelatedField(
        queryset=Sucursal.objects.all(), source='sucursal_retiro', write_only=True, allow_null=True, required=False
    )
    direccion_envio = serializers.StringRelatedField(read_only=True)
    sucursal_retiro = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'monto_total', 'tipo_pago', 'tipo_entrega',
                  'direccion_envio', 'direccion_envio_id',
                  'sucursal_retiro', 'sucursal_retiro_id', 'estado',
                  'fecha_pedido', 'items']
        read_only_fields = ['fecha_pedido', 'usuario', 'monto_total']

    def create(self, validated_data):
        request = self.context.get('request')
        usuario = request.user if request else None  
        items_data = validated_data.pop('items')
        estado = validated_data.pop('estado')
        tipo_pago = validated_data.pop('tipo_pago')
        tipo_entrega = validated_data.pop('tipo_entrega')
        direccion_envio = validated_data.pop('direccion_envio', None)
        sucursal_retiro = validated_data.pop('sucursal_retiro', None)
        monto_total = 0

        # Crear pedido vacío
        pedido = Pedido.objects.create(
            usuario=usuario,
            monto_total=0,
            estado=estado,
            tipo_pago=tipo_pago,
            tipo_entrega=tipo_entrega,
            direccion_envio=direccion_envio,
            sucursal_retiro=sucursal_retiro
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
        estado_anterior = instance.estado
        instance.tipo_entrega = validated_data.get('tipo_entrega', instance.tipo_entrega)
        instance.tipo_pago = validated_data.get('tipo_pago', instance.tipo_pago)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.save()

        if estado_anterior != instance.estado:
            # Notificar si cambió el estado y el usuario tiene fcm_token
            if instance.usuario.fcm_token:
                try:
                    enviar_notificacion_fcm(
                        token=instance.usuario.fcm_token,
                        titulo="📢 Estado de tu pedido actualizado",
                        mensaje=f"Tu pedido cambió a estado: {instance.estado}"
                    )
                except Exception as e:
                    print(f"Error al enviar notificación FCM: {e}")

            # Crear notificación en BD si la estás usando
            from notificaciones.models import Notificacion
            Notificacion.objects.create(
                usuario=instance.usuario,
                pedido=instance,
                mensaje=f"📢 Tu pedido #{instance.id} cambió a estado: {instance.estado}"
            )

        return instance

