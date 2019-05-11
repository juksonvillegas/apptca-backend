from django.db import models
from personas.models import Persona
from productos.models import Producto
import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Compra(models.Model):
    proveedor = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True)
    flete = models.DecimalField( max_digits=5, decimal_places=2, default = 0)
    estado = models.BooleanField(default = True)
    def __str__(self):
        return str(self.fecha)

class Compra_detalle(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    costo = models.DecimalField( max_digits=5, decimal_places=2, default = 0)
    estado = models.BooleanField(default = True)
    def __str__(self):
        return str(self.cantidad)

@receiver(post_save, sender=Compra_detalle)
def save_compra_detalle(sender, instance, **kwargs):
    prod = Producto.objects.get(id=instance.producto.id)
    costototal = (prod.stock * prod.costo) + (instance.cantidad * instance.costo)
    stocktotal = prod.stock * instance.cantidad
    prod.costo = costototal / stocktotal
    prod.stock +=instance.cantidad
    prod.save()
    print('stock actualizado=' + str(prod.stock))
    
@receiver(post_delete, sender=Compra_detalle)
def delete_compra_detalle(sender, instance, **kwargs):
    prod = Producto.objects.get(id=instance.producto.id)
    costototal = (prod.stock * prod.costo) - (instance.cantidad * instance.costo)
    stocktotal = prod.stock * instance.cantidad
    prod.costo = costototal / stocktotal
    prod.stock -=instance.cantidad
    prod.save()
    print('stock actualizado=' + str(prod.stock))