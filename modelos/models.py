from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length = 50)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    extendido = models.CharField(max_length=200, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

