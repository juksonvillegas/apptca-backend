from django.db import models
from personas.models import Persona
from productos.models import Producto
import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.
class Venta(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True)
    estado = models.BooleanField(default = True)
    def __str__(self):
        return str(self.fecha)

class Venta_detalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    precio = models.DecimalField( max_digits=5, decimal_places=2, default = 0)
    estado = models.BooleanField(default = True)
    def __str__(self):
        return str(self.cantidad)

@receiver(post_save, sender=Venta_detalle)
def save_venta_detalle(sender, instance, **kwargs):
    prod = Producto.objects.get(id=instance.producto.id)
    prod.stock -=instance.cantidad
    prod.save()
    print('stock actualizado=' + str(prod.stock))

@receiver(post_delete, sender=Venta_detalle)
def delete_venta_detalle(sender, instance, **kwargs):
    prod = Producto.objects.get(id=instance.producto.id)
    prod.stock +=instance.cantidad
    prod.save()
    print('stock actualizado=' + str(prod.stock))