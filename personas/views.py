from personas.models import Persona
from personas.serializers import PersonaSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class PersonasLista(generics.ListCreateAPIView):
    queryset = Persona.objects.filter(proveedor = False).order_by('nombre')
    serializer_class = PersonaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'nombre':['icontains'], 'telefono':['icontains'], 'dni':['icontains'], 'sexo':['exact'] }

class PersonasDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class ProveedorDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.filter(proveedor=True)
    serializer_class = PersonaSerializer

class ProveedoresLista(generics.ListCreateAPIView):
    queryset = Persona.objects.filter(proveedor = True).order_by('nombre')
    serializer_class = PersonaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'nombre':['icontains'], 'telefono':['icontains'], 'dni':['icontains'], 'sexo':['exact'] }

 
