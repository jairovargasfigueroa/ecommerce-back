from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from core.viewsets import BaseViewSet
from .models import Usuario
from .serializers import UsuarioSerializer,CustomTokenObtainPairSerializer

class UsuarioViewSet(BaseViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    basename = 'usuarios'

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer