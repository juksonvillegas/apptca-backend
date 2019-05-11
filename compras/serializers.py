from productos.models import Producto
from categorias.models import Categoria
from modelos.models import Modelo, Marca
from personas.models import Persona
from compras.models import Compra, Compra_detalle
from rest_framework import serializers

class Compra_DetalleSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='producto.categoria.nombre', required=False, read_only=True)
    modelo = serializers.CharField(source='producto.modelo.nombre', required=False, read_only=True)
    marca = serializers.CharField(source='producto.modelo.marca.nombre', required=False, read_only=True)
    class Meta:
        model = Compra_detalle
        fields = ('id', 'compra', 'producto', 'cantidad', 'costo', 'estado', 'modelo', 'marca', 'categoria')

class CompraSerializer(serializers.ModelSerializer):
    proveedor_nombre = serializers.CharField(source='proveedor.nombre', required=False, read_only=True)
    class Meta:
        model = Compra
        fields = ('id','proveedor', 'proveedor_nombre', 'flete', 'fecha', 'estado')
    def create(self, validated_data):
        compra = Compra.objects.create(**validated_data)
        return compra
