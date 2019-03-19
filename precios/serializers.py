from precios.models import Precio
from rest_framework import serializers

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ('id', 'nombre', 'unitario', 'punto', 'docena', 'estado')