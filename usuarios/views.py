from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

from rest_framework import viewsets, permissions
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAdminUser]  # Solo el admin puede ver todos los usuarios

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer