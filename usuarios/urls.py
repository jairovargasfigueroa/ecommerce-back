from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LoginView, UsuarioViewSet, DireccionesEnvioView, DireccionEnvioDetalleView, ActualizarTokenFCMView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuarios')

urlpatterns = [

    path('login/', LoginView.as_view(), name='custom_login'),


    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('direcciones-envio/', DireccionesEnvioView.as_view(), name='lista-direcciones'),
    path('direcciones-envio/<int:pk>/', DireccionEnvioDetalleView.as_view(), name='detalle-direccion'),
    path('actualizar-token/', ActualizarTokenFCMView.as_view()),
]

# Agregamos las rutas del router al final
urlpatterns += router.urls
