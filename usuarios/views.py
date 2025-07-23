from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from core.viewsets import BaseViewSet
from .models import Usuario, DireccionEnvio
from .serializers import UsuarioSerializer, CustomTokenObtainPairSerializer, DireccionEnvioSerializer


class UsuarioViewSet(BaseViewSet):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    basename = 'usuarios'

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class DireccionesEnvioView(generics.ListCreateAPIView):
    serializer_class = DireccionEnvioSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return DireccionEnvio.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class DireccionEnvioDetalleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DireccionEnvioSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return DireccionEnvio.objects.filter(usuario=self.request.user)


class ActualizarTokenFCMView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        token = request.data.get('fcm_token')
        if token:
            usuario = request.user
            usuario.fcm_token = token
            usuario.save()
            print(token)
            return Response({'mensaje': 'Token actualizado correctamente'})
        return Response({'error': 'Faltó el token'}, status=400)
