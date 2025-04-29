import os
import django
import random
from faker import Faker
from datetime import timedelta
from django.utils import timezone
import sys

# Configuración de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from productos.models import Producto
from usuarios.models import Usuario
from pedidos.models import Pedido, ItemPedido

fake = Faker("es_CO")

# 🔹 Categorías desde tu modelo Producto
CATEGORIAS = [cat[0] for cat in Producto.CATEGORIAS]

PRODUCTOS_DATA = [
    # Teléfonos
    {"nombre": "iPhone 14 Pro", "categoria": "telefonos", "precio": 1200, "descripcion": "Smartphone Apple 128GB", "stock": 65},
    {"nombre": "Samsung Galaxy S23", "categoria": "telefonos", "precio": 999, "descripcion": "Teléfono Samsung gama alta", "stock": 58},
    {"nombre": "Xiaomi Redmi Note 12", "categoria": "telefonos", "precio": 350, "descripcion": "Smartphone económico potente", "stock": 70},
    {"nombre": "Motorola Edge 30", "categoria": "telefonos", "precio": 450, "descripcion": "Teléfono con pantalla OLED", "stock": 55},
    {"nombre": "Google Pixel 7", "categoria": "telefonos", "precio": 799, "descripcion": "Smartphone con Android puro", "stock": 60},

    # Laptops
    {"nombre": "MacBook Air M2", "categoria": "laptops", "precio": 1500, "descripcion": "Portátil ultraligero Apple", "stock": 52},
    {"nombre": "Lenovo ThinkPad X1", "categoria": "laptops", "precio": 1300, "descripcion": "Laptop empresarial resistente", "stock": 67},
    {"nombre": "HP Pavilion 15", "categoria": "laptops", "precio": 750, "descripcion": "Laptop para uso diario", "stock": 59},
    {"nombre": "Dell XPS 13", "categoria": "laptops", "precio": 1400, "descripcion": "Ultrabook premium de Dell", "stock": 54},
    {"nombre": "Asus ROG Strix", "categoria": "laptops", "precio": 1600, "descripcion": "Laptop gamer de alto rendimiento", "stock": 61},

    # Tablets
    {"nombre": "iPad 10ª Gen", "categoria": "tablets", "precio": 500, "descripcion": "Tablet versátil Apple", "stock": 63},
    {"nombre": "Samsung Galaxy Tab S8", "categoria": "tablets", "precio": 700, "descripcion": "Tablet Android de gama alta", "stock": 57},
    {"nombre": "Lenovo Tab P11", "categoria": "tablets", "precio": 300, "descripcion": "Tablet económica para multimedia", "stock": 68},
    {"nombre": "Huawei MatePad 11", "categoria": "tablets", "precio": 450, "descripcion": "Tablet con stylus incluido", "stock": 55},
    {"nombre": "Amazon Fire HD 10", "categoria": "tablets", "precio": 180, "descripcion": "Tablet básica para entretenimiento", "stock": 70},

    # Auriculares
    {"nombre": "Sony WH-1000XM5", "categoria": "auriculares", "precio": 400, "descripcion": "Auriculares con cancelación de ruido", "stock": 53},
    {"nombre": "AirPods Pro 2", "categoria": "auriculares", "precio": 250, "descripcion": "Auriculares inalámbricos Apple", "stock": 60},
    {"nombre": "JBL Tune 510BT", "categoria": "auriculares", "precio": 60, "descripcion": "Auriculares Bluetooth económicos", "stock": 69},
    {"nombre": "Beats Studio3", "categoria": "auriculares", "precio": 300, "descripcion": "Auriculares premium para música", "stock": 51},
    {"nombre": "Logitech G Pro X", "categoria": "auriculares", "precio": 120, "descripcion": "Auriculares gamer profesionales", "stock": 66},

    # Consolas
    {"nombre": "PlayStation 5", "categoria": "consolas", "precio": 600, "descripcion": "Consola de última generación", "stock": 55},
    {"nombre": "Xbox Series X", "categoria": "consolas", "precio": 580, "descripcion": "Consola potente de Microsoft", "stock": 52},
    {"nombre": "Nintendo Switch OLED", "categoria": "consolas", "precio": 400, "descripcion": "Consola híbrida portátil", "stock": 60},
    {"nombre": "Steam Deck", "categoria": "consolas", "precio": 500, "descripcion": "Consola portátil para PC gaming", "stock": 58},
    {"nombre": "Nintendo Switch Lite", "categoria": "consolas", "precio": 250, "descripcion": "Versión compacta de la Switch", "stock": 65},

    # Monitores
    {"nombre": "LG UltraWide 34\"", "categoria": "monitores", "precio": 650, "descripcion": "Monitor panorámico para productividad", "stock": 59},
    {"nombre": "Samsung Odyssey G5", "categoria": "monitores", "precio": 500, "descripcion": "Monitor curvo gamer", "stock": 54},
    {"nombre": "Dell UltraSharp 27\"", "categoria": "monitores", "precio": 700, "descripcion": "Monitor profesional de alta resolución", "stock": 56},
    {"nombre": "Asus TUF Gaming 24\"", "categoria": "monitores", "precio": 300, "descripcion": "Monitor gamer económico", "stock": 67},
    {"nombre": "Acer Nitro VG270", "categoria": "monitores", "precio": 350, "descripcion": "Monitor IPS Full HD", "stock": 60},

    # Almacenamiento
    {"nombre": "Samsung SSD 1TB", "categoria": "almacenamiento", "precio": 150, "descripcion": "Disco sólido NVMe", "stock": 62},
    {"nombre": "WD My Passport 2TB", "categoria": "almacenamiento", "precio": 90, "descripcion": "Disco duro portátil", "stock": 70},
    {"nombre": "Seagate Barracuda 4TB", "categoria": "almacenamiento", "precio": 120, "descripcion": "Disco duro interno", "stock": 55},
    {"nombre": "Kingston SSD 480GB", "categoria": "almacenamiento", "precio": 80, "descripcion": "Disco sólido económico", "stock": 66},
    {"nombre": "SanDisk Ultra 128GB", "categoria": "almacenamiento", "precio": 30, "descripcion": "Pendrive USB 3.0", "stock": 68},

    # Redes
    {"nombre": "Router TP-Link AX1800", "categoria": "redes", "precio": 120, "descripcion": "Router WiFi 6", "stock": 53},
    {"nombre": "Router Asus RT-AX86U", "categoria": "redes", "precio": 250, "descripcion": "Router gamer WiFi 6", "stock": 57},
    {"nombre": "Extensor TP-Link RE450", "categoria": "redes", "precio": 70, "descripcion": "Amplificador de señal WiFi", "stock": 65},
    {"nombre": "Google Nest WiFi", "categoria": "redes", "precio": 300, "descripcion": "Sistema de red mallada", "stock": 60},
    {"nombre": "Módem Netgear CM500", "categoria": "redes", "precio": 100, "descripcion": "Módem cableado", "stock": 69},

    # Hogar Inteligente
    {"nombre": "Amazon Echo Dot", "categoria": "hogar_smart", "precio": 50, "descripcion": "Asistente inteligente", "stock": 70},
    {"nombre": "Google Nest Hub", "categoria": "hogar_smart", "precio": 90, "descripcion": "Pantalla inteligente", "stock": 55},
    {"nombre": "Enchufe Inteligente TP-Link", "categoria": "hogar_smart", "precio": 25, "descripcion": "Control remoto de dispositivos", "stock": 68},
    {"nombre": "Xiaomi Mi LED Smart Bulb", "categoria": "hogar_smart", "precio": 20, "descripcion": "Bombilla inteligente RGB", "stock": 66},
    {"nombre": "Cámara Ring Indoor Cam", "categoria": "hogar_smart", "precio": 60, "descripcion": "Cámara de seguridad WiFi", "stock": 58},

    # Otros (Componentes, Cables, Periféricos, etc.)
    {"nombre": "Teclado Mecánico Redragon", "categoria": "perifericos", "precio": 70, "descripcion": "Teclado gamer retroiluminado", "stock": 63},
    {"nombre": "Mouse Logitech MX Master 3", "categoria": "perifericos", "precio": 100, "descripcion": "Ratón ergonómico profesional", "stock": 61},
    {"nombre": "Fuente Corsair 650W", "categoria": "componentes", "precio": 120, "descripcion": "Fuente de poder certificada", "stock": 54},
    {"nombre": "Tarjeta Gráfica RTX 3060", "categoria": "componentes", "precio": 400, "descripcion": "GPU para gaming", "stock": 52},
    {"nombre": "Cable HDMI 4K 2m", "categoria": "cables", "precio": 15, "descripcion": "Cable de alta velocidad", "stock": 70},
    {"nombre": "Adaptador USB-C a HDMI", "categoria": "cables", "precio": 25, "descripcion": "Adaptador multipropósito", "stock": 68},
    {"nombre": "Power Bank Xiaomi 20000mAh", "categoria": "powerbank", "precio": 45, "descripcion": "Batería externa de gran capacidad", "stock": 66},
    {"nombre": "Proyector Epson X41", "categoria": "proyectores", "precio": 550, "descripcion": "Proyector para oficina y hogar", "stock": 59},
    {"nombre": "Drone DJI Mini 2", "categoria": "drones", "precio": 500, "descripcion": "Drone compacto con cámara 4K", "stock": 60},

    # Camaras
    {"nombre": "Canon EOS R6", "categoria": "camaras", "precio": 2400, "descripcion": "Cámara mirrorless profesional", "stock": 55},
    {"nombre": "Sony Alpha a6400", "categoria": "camaras", "precio": 1400, "descripcion": "Cámara compacta de lentes intercambiables", "stock": 53},
    {"nombre": "GoPro HERO11 Black", "categoria": "camaras", "precio": 500, "descripcion": "Cámara de acción 5K", "stock": 60},
    {"nombre": "DJI Osmo Pocket 2", "categoria": "camaras", "precio": 350, "descripcion": "Cámara portátil con estabilizador", "stock": 58},
    {"nombre": "Nikon Z50", "categoria": "camaras", "precio": 1100, "descripcion": "Cámara mirrorless liviana", "stock": 61},

    # wearables
    {"nombre": "Apple Watch Series 9", "categoria": "wearables", "precio": 450, "descripcion": "Smartwatch con monitor de salud", "stock": 66},
    {"nombre": "Samsung Galaxy Watch 6", "categoria": "wearables", "precio": 400, "descripcion": "Reloj inteligente deportivo", "stock": 65},
    {"nombre": "Fitbit Charge 6", "categoria": "wearables", "precio": 180, "descripcion": "Pulsera fitness de alta duración", "stock": 60},
    {"nombre": "Huawei Watch GT 4", "categoria": "wearables", "precio": 250, "descripcion": "Smartwatch de batería prolongada", "stock": 64},
    {"nombre": "Amazfit GTR 4", "categoria": "wearables", "precio": 220, "descripcion": "Reloj inteligente para entrenamiento", "stock": 62},

    # tv
    {"nombre": "Samsung QLED 55\"", "categoria": "tv", "precio": 1200, "descripcion": "Televisor 4K con HDR", "stock": 58},
    {"nombre": "LG OLED 65\"", "categoria": "tv", "precio": 2000, "descripcion": "Televisor OLED de alta gama", "stock": 55},
    {"nombre": "Sony Bravia 55\"", "categoria": "tv", "precio": 1500, "descripcion": "Televisor con Android TV", "stock": 60},
    {"nombre": "TCL 4K UHD 50\"", "categoria": "tv", "precio": 600, "descripcion": "Televisor económico con buena calidad", "stock": 65},
    {"nombre": "Xiaomi Mi TV 43\"", "categoria": "tv", "precio": 400, "descripcion": "Televisor inteligente de 43 pulgadas", "stock": 70},
    
    # cargadores
    {"nombre": "Cargador Anker 20W", "categoria": "cargadores", "precio": 25, "descripcion": "Cargador rápido USB-C", "stock": 68},
    {"nombre": "Cargador Inalámbrico Belkin", "categoria": "cargadores", "precio": 40, "descripcion": "Cargador inalámbrico para móviles", "stock": 65},
    {"nombre": "Cargador Rápido Aukey", "categoria": "cargadores", "precio": 35, "descripcion": "Cargador rápido de 30W", "stock": 70},
    {"nombre": "Cargador de Pared Baseus", "categoria": "cargadores", "precio": 20, "descripcion": "Cargador compacto y rápido", "stock": 66},
    {"nombre": "Cargador de Coche Anker", "categoria": "cargadores", "precio": 30, "descripcion": "Cargador para coche con 2 puertos", "stock": 64},  
    
    # cables
    {"nombre": "Cable USB-C a USB-C 1m", "categoria": "cables", "precio": 10, "descripcion": "Cable de carga rápida", "stock": 70},
    {"nombre": "Cable HDMI 2.0 2m", "categoria": "cables", "precio": 15, "descripcion": "Cable HDMI de alta velocidad", "stock": 68},
    {"nombre": "Cable Ethernet Cat 6", "categoria": "cables", "precio": 12, "descripcion": "Cable de red de alta velocidad", "stock": 65},
    {"nombre": "Cable Lightning a USB", "categoria": "cables", "precio": 18, "descripcion": "Cable para dispositivos Apple", "stock": 66},
    {"nombre": "Cable Auxiliar 3.5mm", "categoria": "cables", "precio": 8, "descripcion": "Cable de audio auxiliar", "stock": 70},
    {"nombre": "Cable USB 3.0 a USB-C", "categoria": "cables", "precio": 12, "descripcion": "Cable de transferencia rápida", "stock": 64},
    {"nombre": "Cable de Alimentación 1.5m", "categoria": "cables", "precio": 10, "descripcion": "Cable de alimentación universal", "stock": 62},
    {"nombre": "Cable VGA a HDMI", "categoria": "cables", "precio": 20, "descripcion": "Adaptador de video", "stock": 63},
    {"nombre": "Cable DisplayPort a HDMI", "categoria": "cables", "precio": 25, "descripcion": "Cable de video para monitores", "stock": 61},
    {"nombre": "Cable USB-C a HDMI 2m", "categoria": "cables", "precio": 30, "descripcion": "Cable de video para dispositivos USB-C", "stock": 60},
    {"nombre": "Cable Micro USB 1m", "categoria": "cables", "precio": 5, "descripcion": "Cable de carga y transferencia", "stock": 70},
    
    # Accesorios para Móviles
    {"nombre": "Funda iPhone 14", "categoria": "acc_movil", "precio": 25, "descripcion": "Funda de silicona para iPhone", "stock": 68},
    {"nombre": "Protector de Pantalla Galaxy S23", "categoria": "acc_movil", "precio": 15, "descripcion": "Protector de telefono", "stock": 70},
    {"nombre": "Soporte para Móvil", "categoria": "acc_movil", "precio": 20, "descripcion": "Soporte ajustable para coche", "stock": 65},
    {"nombre": "Funda Samsung Galaxy S23", "categoria": "acc_movil", "precio": 20, "descripcion": "Funda resistente al agua", "stock": 61},
    {"nombre": "Adaptador de Audio Bluetooth", "categoria": "acc_movil", "precio": 35, "descripcion": "Adaptador para conectar auriculares", "stock": 60},
    {"nombre": "Luz LED para Selfies", "categoria": "acc_movil", "precio": 12, "descripcion": "Anillo de luz para selfies", "stock": 70},
        
    #impresoras
    {"nombre": "Impresora HP LaserJet Pro", "categoria": "impresoras", "precio": 200, "descripcion": "Impresora láser rápida", "stock": 65},
    {"nombre": "Impresora Canon PIXMA", "categoria": "impresoras", "precio": 150, "descripcion": "Impresora multifuncional", "stock": 60},
    {"nombre": "Impresora Epson EcoTank", "categoria": "impresoras", "precio": 250, "descripcion": "Impresora de tinta recargable", "stock": 70},
    {"nombre": "Escáner Fujitsu ScanSnap", "categoria": "impresoras", "precio": 300, "descripcion": "Escáner portátil rápido", "stock": 55},
    {"nombre": "Impresora Brother MFC-L3770CDW", "categoria": "impresoras", "precio": 400, "descripcion": "Impresora láser color multifuncional", "stock": 58},
    
    # acc_pc
    {"nombre": "Teclado Logitech K380", "categoria": "acc_pc", "precio": 50, "descripcion": "Teclado inalámbrico compacto", "stock": 65},
    {"nombre": "Mouse Razer DeathAdder", "categoria": "acc_pc", "precio": 70, "descripcion": "Ratón gamer ergonómico", "stock": 60},
    {"nombre": "Webcam Logitech C920", "categoria": "acc_pc", "precio": 100, "descripcion": "Cámara web Full HD", "stock": 70},
    {"nombre": "Alfombrilla Razer Firefly", "categoria": "acc_pc", "precio": 40, "descripcion": "Alfombrilla gamer RGB", "stock": 66},
    {"nombre": "Micrófono Blue Yeti", "categoria": "acc_pc", "precio": 130, "descripcion": "Micrófono USB de calidad profesional", "stock": 68},
    
    # redes
    {"nombre": "Router TP-Link Archer AX50", "categoria": "redes", "precio": 150, "descripcion": "Router WiFi 6 de alto rendimiento", "stock": 65},
    {"nombre": "Switch Netgear GS308", "categoria": "redes", "precio": 80, "descripcion": "Switch de 8 puertos Gigabit", "stock": 60},
    {"nombre": "Adaptador TP-Link USB WiFi", "categoria": "redes", "precio": 30, "descripcion": "Adaptador USB para WiFi", "stock": 70},
    {"nombre": "Repetidor WiFi TP-Link RE305", "categoria": "redes", "precio": 50, "descripcion": "Repetidor de señal WiFi", "stock": 66},
    {"nombre": "Módem Arris SURFboard SB8200", "categoria": "redes", "precio": 200, "descripcion": "Módem DOCSIS 3.1", "stock": 68},

]

# 🚨 Limpieza previa (opcional en entorno de pruebas)
def limpiar_datos():
    Producto.objects.all().delete()
    Usuario.objects.filter(rol='cliente').delete()
    Pedido.objects.all().delete()
    ItemPedido.objects.all().delete()
    print("🧹 Datos anteriores eliminados.")

# 🔹 1. Crear Productos
def crear_productos():
    fecha_base = timezone.now() - timedelta(days=180)  # Hace 6 meses exactos

    for producto in PRODUCTOS_DATA:
        # Generar una fecha aleatoria entre hace 6 meses y hace 5 meses (180 a 150 días atrás)
        dias_random = random.randint(0, 30)  # 0 a 30 días
        fecha_random = fecha_base + timedelta(days=dias_random)

        prod = Producto.objects.create(
            nombre=producto["nombre"],
            descripcion=producto["descripcion"],
            precio=producto["precio"],
            stock=producto["stock"],
            categoria=producto["categoria"],
            imagen=None
        )

        # Forzar manualmente la fecha aleatoria
        prod.fecha_creacion = fecha_random
        prod.save()

    print(f"✅ {len(PRODUCTOS_DATA)} Productos creados correctamente con fechas distribuidas entre 6 y 5 meses atrás.")

    # 🔹 2. Crear usuarios
def crear_clientes():
    for _ in range(100):
        Usuario.objects.create_user(
            username=fake.unique.user_name(),
            email=fake.unique.email(),
            password="Test1234",
            rol="cliente"
        )
    print("✅ 100 Clientes creados correctamente.")
# 🔹 3. Crear pedidos
def crear_pedidos():
    clientes = list(Usuario.objects.filter(rol="cliente"))
    productos = list(Producto.objects.all())

    pedidos_por_mes = 25  # Para 6 meses ➔ 150 pedidos aprox
    ahora = timezone.now()

    for mes_offset in range(6):
        fecha_base = ahora - timedelta(days=mes_offset * 30)

        for _ in range(pedidos_por_mes):
            cliente = random.choice(clientes)
            fecha_pedido = fecha_base - timedelta(days=random.randint(0, 29))
            pedido = Pedido.objects.create(
                usuario=cliente,
                monto_total=0,
                estado=random.choice(['completado', 'cancelado']),
                tipo_pago=random.choice(['tarjeta', 'qr', 'efectivo']),
                tipo_entrega=random.choice(['delivery', 'tienda']),
                fecha_pedido=fecha_pedido
            )

            total = 0
            items_count = random.randint(3, 7)
            productos_seleccionados = random.sample(productos, items_count)

            for producto in productos_seleccionados:
                cantidad = random.randint(1, 3)
                ItemPedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio
                )
                total += cantidad * float(producto.precio)

            pedido.monto_total = total
            pedido.save()

    print("✅ Pedidos generados correctamente.")

# 🚀 Ejecutar todo
if __name__ == "__main__":
    limpiar_datos()
    crear_productos()
    crear_clientes()
    crear_pedidos()