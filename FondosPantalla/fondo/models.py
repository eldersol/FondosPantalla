
from django.db import models

class Fondos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    activa = models.BooleanField()
    imagen = models.ImageField(upload_to="original", null=True)
