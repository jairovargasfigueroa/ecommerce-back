from django.db import models

from productos.models import Producto
from usuarios.models import Usuario


# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el usuario
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Carrito - {self.producto.nombre} - Cantidad:{self.cantidad}"
    
