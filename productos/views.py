from productos.models import Producto
from productos.serializers import ProductoSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductosLista(generics.ListCreateAPIView):
    queryset = Producto.objects.all().order_by('modelo__marca__nombre', 'modelo__nombre')
    serializer_class = ProductoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'modelo__nombre':['icontains'], 'modelo__marca__nombre':['icontains'] }

class ProductoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer