from django.db import models

from productos.models import Producto
from usuarios.models import Usuario


class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE ,related_name='pedidos')
    monto_total = models.DecimalField(max_digits=10,decimal_places=2)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado')
    ])
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL,null=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
# Create your models here.
