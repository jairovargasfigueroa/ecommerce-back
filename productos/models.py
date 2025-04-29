from django.db import models
from storage_backend.azure_sas_storage import azure_storage   # Importa la instancia
class Producto(models.Model):
    CATEGORIAS = [
        ('telefonos', 'Teléfonos y Smartphones'),
        ('laptops', 'Laptops y Notebooks'),
        ('tablets', 'Tablets'),
        ('acc_movil', 'Accesorios para Móviles'),
        ('acc_pc', 'Accesorios para Computadoras'),
        ('auriculares', 'Auriculares y Audífonos'),
        ('camaras', 'Cámaras y Fotografía'),
        ('wearables', 'Smartwatches y Wearables'),
        ('consolas', 'Consolas y Videojuegos'),
        ('tv', 'Televisores y Pantallas'),
        ('audio', 'Audio y Sonido'),
        ('drones', 'Drones'),
        ('almacenamiento', 'Almacenamiento'),
        ('impresoras', 'Impresoras y Escáneres'),
        ('redes', 'Routers y Redes'),
        ('componentes', 'Componentes de PC'),
        ('electro_inteligente', 'Electrodomésticos Inteligentes'),
        ('monitores', 'Monitores'),
        ('proyectores', 'Proyectores'),
        ('cargadores', 'Cargadores y Baterías'),
        ('perifericos', 'Periféricos'),
        ('hogar_smart', 'Hogar Inteligente'),
        ('powerbank', 'Power Banks'),
        ('software', 'Software y Licencias'),
        ('cables', 'Cables y Adaptadores'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/', storage=azure_storage)
    categoria = models.CharField(max_length=100,choices=CATEGORIAS, default='telefonos')

    def __str__(self):
        return self.nombre

