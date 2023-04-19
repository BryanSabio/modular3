from django.db import models 
import datetime

# Create your models here.

class ProductoPequeno(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=200)
    adquirir = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__ (self):
        return self.nombre
    
class ProductoMediano(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=200)
    adquirir = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__ (self):
        return self.nombre
    
class ProductoGrande(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=200)
    adquirir = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__ (self):
        return self.nombre
    
class ProductoGigante(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=200)
    adquirir = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__ (self):
        return self.nombre



    '''class Meta:
        indexes = [
                models.Index(fields=['venta', 'producto',]),
            ]'''