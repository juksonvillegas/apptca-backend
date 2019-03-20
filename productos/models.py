from django.db import models
from modelos.models import Modelo
from categorias.models import Categoria
from precios.models import Precio

class Producto(models.Model):
    nombre = models.CharField(max_length = 50, blank = True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
    stock = models.IntegerField(default = 0)
    costo = models.DecimalField( max_digits=5, decimal_places=2, default = 0)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre