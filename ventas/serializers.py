from productos.models import Producto
from categorias.models import Categoria
from modelos.models import Modelo, Marca
from personas.models import Persona
from ventas.models import Venta, Venta_detalle
from rest_framework import serializers

class Venta_DetalleSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='producto.categoria.nombre', required=False, read_only=True)
    modelo = serializers.CharField(source='producto.modelo.nombre', required=False, read_only=True)
    marca = serializers.CharField(source='producto.modelo.marca.nombre', required=False, read_only=True)
    class Meta:
        model = Venta_detalle
        fields = ('id', 'venta', 'producto', 'cantidad', 'precio', 'estado', 'modelo', 'marca', 'categoria')

class VentaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', required=False, read_only=True)
    class Meta:
        model = Venta
        fields = ('id','cliente', 'cliente_nombre', 'fecha', 'estado')
    def create(self, validated_data):
        venta = Venta.objects.create(**validated_data)
        return venta
