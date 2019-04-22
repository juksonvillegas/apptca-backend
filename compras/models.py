from django.db import models
from personas.models import Persona
from productos.models import Producto
import datetime

class Compra(models.Model):
    proveedor = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    flete = models.DecimalField( max_digits=5, decimal_places=2, default = 0)
    estado = models.BooleanField(default = True)

class Compra_detalle(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    costo = models.DecimalField( max_digits=5, decimal_places=2, default = 0)
    estado = models.BooleanField(default = True)
    