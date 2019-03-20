from productos.models import Producto
from modelos.models import Modelo, Marca
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    modelo_nombre = serializers.CharField(source='modelo', required=False, read_only=True)
    marca_nombre = serializers.CharField(source='modelo.marca.nombre', required=False, read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', required=False, read_only=True)
    precio_unitario = serializers.CharField(source='precio.unitario', required=False, read_only=True)
    precio_punto = serializers.CharField(source='precio.punto', required=False, read_only=True)
    precio_docena = serializers.CharField(source='precio.docena', required=False, read_only=True)
    class Meta:
        model = Producto
        fields = ('id','nombre', 'modelo', 'modelo_nombre', 'marca_nombre', 'categoria', 
        'categoria_nombre', 'precio', 'precio_unitario', 'precio_punto', 'precio_docena', 'estado')