from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    tipo_empleado = (
        ('v','Vendedor'),
        ('a','Administrador'),
    )
    tipo = models.CharField(
        max_length= 1, 
        choices=tipo_empleado,
        default='v',
    )
    estado_disponibilidad = (
        ('a','Activo'),
        ('i','Inactivo'),
    )
    disponibilidad = models.CharField(
        max_length= 1,
        choices=estado_disponibilidad,
        default= 'a',
    )
    creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='usuarios'
        verbose_name_plural='usuarios'


    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)