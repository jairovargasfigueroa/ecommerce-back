from django.db import models
from storage_backend.azure_sas_storage import azure_storage   # Importa la instancia
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/', storage=azure_storage)

    def __str__(self):
        return self.nombre

# Create your models here.
