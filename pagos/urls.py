from django.urls import path
from .views import CrearSesionPagoView, create_payment_intent

urlpatterns = [
    path('crear-sesion-pago/', CrearSesionPagoView.as_view(), name='crear_sesion_pago'),
    path('create-payment-intent/', create_payment_intent, name='create-payment-intent'),
]
