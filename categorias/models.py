from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
