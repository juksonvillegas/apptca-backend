from django.shortcuts import render
from ventas.models import Venta, Venta_detalle
from ventas.serializers import VentaSerializer, Venta_DetalleSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class VentasLista(generics.ListCreateAPIView):
    queryset = Venta.objects.all().order_by('-fecha')
    serializer_class = VentaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'cliente', 'fecha' }

class VentasDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class Venta_detalleLista(generics.ListCreateAPIView):
    queryset = Venta_detalle.objects.all().order_by('id')
    serializer_class = Venta_DetalleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'venta', 'producto' }

class Venta_detalleDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta_detalle.objects.all()
    serializer_class = Venta_DetalleSerializer