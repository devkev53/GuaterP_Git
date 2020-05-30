from django.db import models

# Create your models here.
TIPO_TELEFONO_CHOICES = [
    ('1', 'Fijo'),
    ('2', 'Movil'),
]
EMPRESA_CHOICES = [
    ('1', 'Claro'),
    ('2', 'Movistar'),
    ('3', 'Tigo'),
]

class Contacto(models.Model):
    numero = models.PositiveIntegerField('Numero')
    tipo = models.PositiveSmallIntegerField('Tipo', choices=TIPO_TELEFONO_CHOICES)
    empresa = models.PositiveSmallIntegerField('Tipo', choices=EMPRESA_CHOICES)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return '%s' % (self.numero)
