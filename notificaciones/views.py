from django.shortcuts import render
from core.viewsets import BaseViewSet
from .models import Notificacion
from .serializers import NotificacionSerializer
from rest_framework.permissions import IsAuthenticated

class NotificacionViewSet(BaseViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    basename = 'notificaciones'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notificacion.objects.filter(usuario=self.request.user).order_by('-fecha')

