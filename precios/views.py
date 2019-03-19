from precios.models import Precio
from precios.serializers import PrecioSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class PreciosLista(generics.ListCreateAPIView):
    queryset = Precio.objects.all().order_by('nombre')
    serializer_class = PrecioSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'nombre':['icontains'] }

class PrecioDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer