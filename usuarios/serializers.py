from rest_framework import serializers
from .models import Usuario, DireccionEnvio
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class DireccionEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionEnvio
        fields = ['id', 'usuario', 'direccion', 'ciudad', 'departamento', 'pais', 'codigo_postal', 'telefono_contacto']

class UsuarioSerializer(serializers.ModelSerializer):
    direcciones_envio = DireccionEnvioSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'rol', 'direcciones_envio']
        extra_kwargs = {
            'password': {'write_only': True},
            'rol': {'required': False}
        }

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        token['username'] = user.username
        token['rol'] = user.rol
        
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['rol'] = self.user.rol
        return data