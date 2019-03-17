from modelos.models import Marca, Modelo
from rest_framework import serializers

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id','nombre','estado')

class ModeloSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source='marca.nombre', required=False, read_only=True)
    class Meta:
        model = Modelo
        fields = ('id','nombre', 'extendido', 'marca' ,'estado', 'marca_nombre')