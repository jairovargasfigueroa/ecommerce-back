from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import ProductoViewSet

router = DefaultRouter()
router.register(r'', ProductoViewSet, basename = 'productos') 


urlpatterns = [
    path('', include(router.urls)),  # Incluye las URLs del router)
]
