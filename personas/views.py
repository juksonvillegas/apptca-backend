from personas.models import Persona
from personas.serializers import PersonaSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class PersonasLista(generics.ListCreateAPIView):
    queryset = Persona.objects.filter().order_by('nombre')
    serializer_class = PersonaSerializer
    filter_backends = (DjangoFilterBackend,)
    #filterset_fields = { 'nombre':['icontains'], 'telefono':['icontains'], 'dni':['icontains'], 'sexo':['exact'] }
    filterset_fields = { 'nombre':['icontains']}

class PersonasDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
 
