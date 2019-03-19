from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class CategoriasLista(generics.ListCreateAPIView):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = { 'nombre':['icontains'] }

class CategoriaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer