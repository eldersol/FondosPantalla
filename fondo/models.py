from django.db import models

# Create your models here.
class Fondos(models.Model):
    titulo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)
    #precio = models.DecimalField(max_digits=4, decimal_places=3)
    activa = models.BooleanField()
