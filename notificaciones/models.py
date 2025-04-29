from django.db import models
from django.db import models
from usuarios.models import Usuario
from pedidos.models import Pedido

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notif {self.usuario.username} - {self.mensaje[:30]}"

