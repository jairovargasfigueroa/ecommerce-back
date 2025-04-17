
from rest_framework import serializers
from .models import Carrito


class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        #fields = '__all__'
        fields = ['id', 'producto', 'cantidad', 'fecha_agregado']