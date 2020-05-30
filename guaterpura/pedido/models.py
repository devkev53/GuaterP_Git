from django.db import models
import datetime

from django.core.exceptions import ValidationError

from cliente.models import Cliente
from producto.models import Producto
from perfil.models import Empleado
from venta.models import Venta

# Create your models here.

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    fecha = models.DateField('Fecha', auto_now_add=True)
    hora_s = models.DateTimeField('Hora de Solicitud', auto_now_add=True)
    repartidor = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name='Repartidor')
    hora_e = models.DateTimeField('Hora de Entrega', auto_now=True)
    descuento = models.FloatField('Descuento', default=0)
    subtotal = models.FloatField('Subtotal', default=0)
    total = models.FloatField('Monto total del Pedido', default=0)
    estado = models.BooleanField('Estado', default=False)

    def suma_sub(self):
        sub_total = 0
        desc = 0
        for d in Detalle.objects.filter(pedido=self.pk):
            sub_total = sub_total + d.subtotal
            des = desc + d.descuento
        self.descuento = desc
        self.subtotal = sub_total

    def exist_venta(self):
        hoy = datetime.date.today()
        venta = False
        if Venta.objects.filter(fecha_a=hoy, estado=1):
            venta = True
        return venta

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return '%s, %s, %s' % (self.cliente, self.total, self.total)

    def clean(self, **kwargs):
        super(Pedido, self).clean()
        # Si nos retorna falso lanzamos un error
        valor = self.exist_venta()
        if valor is False:
            raise ValidationError('Debe Aperturar Venta para este dia..!')

    def save(self):
        self.suma_sub()
        self.total = self.subtotal - self.descuento
        super(Pedido, self).save()

class Detalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Detalle')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.PositiveIntegerField('Cantidad')
    descuento = models.FloatField('Descuento', default=0)
    subtotal = models.FloatField('Subtotal', default=0)
    total = models.FloatField('Monto total del Pedido', default=0)

    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"

    def __str__(self):
        return '%s - Costo: %s - Cantidad: %s - Subtotal: %s - Total: %s' % (
            self.producto.nombre, self.producto.precio, self.cantidad, self.subtotal, self.total)

    def clean(self, **kwargs):
        super(Detalle, self).clean()
        self.subtotal = float(float(int(self.cantidad)) * float(self.producto.precio))
        self.total = float(self.subtotal) - float(self.descuento)

    def save(self):
        self.subtotal = float(float(int(self.cantidad)) * float(self.producto.precio))
        self.total = float(self.subtotal) - float(self.descuento)
        super(Detalle, self).save()
