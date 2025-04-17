from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarritoViewSet

# Enrutador para generar automáticamente las rutas CRUD
router = DefaultRouter()
router.register(r'carritos', CarritoViewSet, basename='carrito')

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas por el enrutador
]