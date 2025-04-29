from django.db import models
from django.db.models import CASCADE

from categorias.models import Categoria


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

# Create your models here.
