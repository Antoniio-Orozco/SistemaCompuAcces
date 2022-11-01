from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    nit = models.CharField(max_length=10)
    creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='proveedores'
        verbose_name_plural='proveedores'

    def __str__(self):
        return '%s %s' % (self.nombre,self.nit)


class Categoria(models.Model):
    nombre = models.CharField(max_length=45)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)


class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    icono = models.ImageField()
    proveedor = models.ManyToManyField(Proveedor)
    creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='productos'
        verbose_name_plural='productos'

    def __str__(self):
        return '%s' % (self.nombre)

