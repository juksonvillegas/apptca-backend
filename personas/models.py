from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 50, )
    telefono = models.CharField( max_length = 9, blank = True)
    dni = models.CharField(max_length = 8, blank = True)
    mayorista = models.BooleanField(default = False)
    proveedor = models.BooleanField(default = False)
    #falta el campo para el sexo

    def __str__(self):
        return self.nombre