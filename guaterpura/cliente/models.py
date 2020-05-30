from django.db import models

from base.models import Contacto

# Create your models here.
TIPO_CLIENTE_CHOICES = [
    ('1', 'Normal'),
    ('2', 'Distribuidor'),
    ('3', 'Especial'),
]

class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    direccion = models.TextField('Direccion')
    nit = models.CharField('Nit', max_length=10)
    tipo_cliente = models.CharField('Tipo', choices=TIPO_CLIENTE_CHOICES, default='1', max_length=1)
    telefono = models.PositiveIntegerField('Telefono' )

    def tipo_c(self):
        if self.tipo_cliente != '3':
            if self.tipo_cliente == '2':
                return 'Dist'
            elif self.tipo_cliente == '1':
                return 'Norm'
        else:
            return 'Esp'

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s - - Tipo. %s' % (self.nombre, self.tipo_c())