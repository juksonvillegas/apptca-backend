from modelos.models import Marca, Modelo
from modelos.serializers import MarcaSerializer, ModeloSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class MarcasLista(generics.ListCreateAPIView):
    queryset = Marca.objects.all().order_by('nombre')
    serializer_class = MarcaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'nombre':['icontains'] }

class MarcaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModelosLista(generics.ListCreateAPIView):
    queryset = Modelo.objects.all().order_by('marca__nombre')
    serializer_class = ModeloSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'nombre':['icontains'], 'marca__nombre':['icontains'], 'extendido':['icontains'] }

class ModeloDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer