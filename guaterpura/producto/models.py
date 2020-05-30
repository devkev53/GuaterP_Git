from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    precio = models.DecimalField('Precio Venta', max_digits=10, decimal_places=2, default=0.00)
    img = models.ImageField('Imagen', blank=True)
    descripcion = models.TextField('Descripcion')

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return '%s %s' % (self.nombre, self.precio)