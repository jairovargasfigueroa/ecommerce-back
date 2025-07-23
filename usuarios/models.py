from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
        ('delivery', 'Delivery'),
    ]
    
    rol = models.CharField(max_length=10, choices=ROLES, default='cliente')
    fcm_token = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username}"

class DireccionEnvio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones_envio')
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    telefono_contacto = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}"