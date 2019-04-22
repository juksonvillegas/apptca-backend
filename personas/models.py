from django.db import models
import datetime

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 50, )
    telefono = models.CharField( max_length = 9, blank = True)
    dni = models.CharField(max_length = 8, blank = True)
    mayorista = models.BooleanField(default = False)
    proveedor = models.BooleanField(default = False)
    sexo = models.BooleanField(default = True)
    nacimiento = models.DateField(default = datetime.date(1990,1,1))
    estado = models.BooleanField(default = True)
    #falta el campo para el sexo

    def __str__(self):
        return self.nombre