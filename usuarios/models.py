from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
        ('delivery', 'Delivery'),
    ]
    
    rol = models.CharField(max_length=10, choices=ROLES, default='cliente')
    
    def __str__(self):
        return f"{self.username} ({self.rol})"