from django.shortcuts import render
from compras.models import Compra, Compra_detalle
from compras.serializers import CompraSerializer, Compra_DetalleSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class ComprasLista(generics.ListCreateAPIView):
    queryset = Compra.objects.all().order_by('-fecha')
    serializer_class = CompraSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'proveedor', 'fecha' }

class ComprasDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class Compra_detalleLista(generics.ListCreateAPIView):
    queryset = Compra_detalle.objects.all()
    serializer_class = Compra_DetalleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'producto':['icontains'] }

class Compra_detalleDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra_detalle.objects.all()
    serializer_class = Compra_DetalleSerializer