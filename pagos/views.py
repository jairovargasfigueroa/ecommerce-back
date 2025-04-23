import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pedidos.models import Pedido

stripe.api_key = settings.STRIPE_SECRET_KEY

class CrearSesionPagoView(APIView):
    def post(self, request):
        try:
            pedido_id = request.data.get('pedido_id')
            pedido = Pedido.objects.get(id=pedido_id)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': f'Pedido #{pedido.id}',
                        },
                        'unit_amount': int(pedido.monto_total * 100),  # En centavos
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:4200/confirmar-pedido?pago=exitoso',
                cancel_url='http://localhost:4200/confirmar-pedido?pago=fallido',
            )

            return Response({'sessionId': session.id})
        except Pedido.DoesNotExist:
            return Response({'error': 'Pedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
