from django.db import models
# Create your models here.
class Precio(models.Model):
    nombre = models.CharField(max_length = 50)
    unitario = models.DecimalField(max_digits=5, decimal_places=2)
    punto = models.DecimalField(max_digits=5, decimal_places=2)
    docena = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre