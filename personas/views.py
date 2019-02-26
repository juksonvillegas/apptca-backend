from personas.models import Persona
from personas.serializers import PersonaSerializer
from rest_framework import viewsets
from rest_framework import generics

"""
Metodo antiguo
class PersonaViewSet(viewsets.ModelViewSet):    
    Este endpoint permiter ver y editar Personas
    queryset = Persona.objects.all().order_by('nombre')
    serializer_class = PersonaSerializer
"""

class PersonasLista(generics.ListCreateAPIView):
    queryset = Persona.objects.all().order_by('nombre')
    serializer_class = PersonaSerializer

class PersonasDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
 
