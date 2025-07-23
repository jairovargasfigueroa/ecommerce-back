from django.conf import settings
import firebase_admin
from firebase_admin import credentials, messaging
import os

def inicializar_firebase():
    if not firebase_admin._apps:
        ruta_credenciales = os.path.join(
            settings.BASE_DIR,  # ← ya tienes esto en settings.py
            'ecommerce',        # ← porque está dentro de la carpeta principal del proyecto
            'ecommerce-b1392-firebase-adminsdk-fbsvc-5a696710d1.json'
        )
        cred = credentials.Certificate(ruta_credenciales)
        firebase_admin.initialize_app(cred)

def enviar_notificacion_fcm(token, titulo, mensaje):
    inicializar_firebase()

    mensaje_fcm = messaging.Message(
        notification=messaging.Notification(
            title=titulo,
            body=mensaje,
        ),
        token=token,
    )

    response = messaging.send(mensaje_fcm)
    print(f"Notificación enviada: {response}")
    return response
