from personas.models import Persona
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombre', 'telefono', 'dni', 'sexo' , 'mayorista', 'proveedor', 'estado')