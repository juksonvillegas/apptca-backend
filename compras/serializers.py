from productos.models import Producto
from categorias.models import Categoria
from modelos.models import Modelo, Marca
from personas.models import Persona
from compras.models import Compra, Compra_detalle
from rest_framework import serializers

class CompraSerializer(serializers.ModelSerializer):
    proveedor_nombre = serializers.CharField(source='persona.nombre', required=False, read_only=True)
    class Meta:
        model = Compra
        fields = ('id','proveedor', 'proveedor_nombre', 'flete', 'fecha', 'estado')

class Compra_DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra_detalle
        fields = ('id', 'compra', 'producto', 'cantidad', 'costo', 'estado')