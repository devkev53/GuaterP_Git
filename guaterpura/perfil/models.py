from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Puesto(models.Model):
    nombre = models.CharField('Nombre del Puesto', max_length=100)
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2, default=0.00)
    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"

    def __str__(self):
        return '%s' % (self.nombre)


class Empleado(models.Model):
    dpi = models.CharField('DPI', max_length=15, unique=True)
    foto = models.ImageField('Fotografia')
    nombres = models.CharField('Nombres', max_length=150)
    apellidos = models.CharField('Apellidos', max_length=150)
    direccion = models.TextField('Direccion')
    nit = models.CharField('NIT', max_length=9)
    fechaNacimiento = models.DateField('Fecha Nacimiento')
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, verbose_name='Puesto', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario', blank=True, null=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)