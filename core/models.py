from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    link_imagen = models.URLField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
