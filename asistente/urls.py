from django.urls import path
from .views import asistente_voz, audio_a_texto

urlpatterns = [
    path('', asistente_voz, name='asistente_voz'),
    path('voz/', audio_a_texto, name='audio_a_texto')
]
