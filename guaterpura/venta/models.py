from django.db import models

from django.core.exceptions import ValidationError

# Create your models here.
class Venta(models.Model):
    fecha_a = models.DateField('Fecha Apertura', auto_now_add=True, unique=True)
    fecha_c = models.DateField('Fecha Cierre', auto_now=True)
    hora_a = models.TimeField('Hora Apertura', auto_now_add=True)
    hora_c = models.TimeField('Hora Apertura', auto_now=True)
    estado = models.PositiveSmallIntegerField('Estado', default=1)
    saldo_a = models.DecimalField('Monto Apertura', max_digits=10, decimal_places=2, default=0.00)
    saldo_c = models.DecimalField('Monto Cierre', max_digits=10, decimal_places=2, default=0.00)
    caudal_a = models.DecimalField('Caudal Inicial', max_digits=10, decimal_places=2, default=0.00)
    caudal_c = models.DecimalField('Caudal Cierre', max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        ordering = ['fecha_a']
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def monto_vendido(self):
        monto = 0
        # Importamos los modelos de pedidos
        from pedido.models import Pedido, Detalle
        # Aumentamos el caudal a 5 a cada galon vendido
        for p in Pedido.objects.filter(fecha=self.fecha_a):
            monto = p.total + monto
        return monto

    def aumentar_caudalimetro(self):
        caudal = 0
        # Importamos los modelos de pedidos
        from pedido.models import Pedido, Detalle
        # Aumentamos el caudal a 5 a cada galon vendido
        for p in Pedido.objects.filter(fecha=self.fecha_a):
            for det in Detalle.objects.filter(pedido=p):
                # Garrafon se creo con el id 2
                if det.producto.id == 2:
                    caudal = (det.cantidad * 5) + caudal
                # Bolsas se creo con el id 3
                elif det.producto.id == 3:
                    caudal = (det.cantidad * 3) + caudal
        return caudal
        short.description = 'Caudal Utilizado'

    def garrafones_vendidos(self):
        cant = 0
        # Importamos los modelos de pedidos
        from pedido.models import Pedido, Detalle
        for p in Pedido.objects.filter(fecha=self.fecha_a):
            for det in Detalle.objects.filter(pedido=p):
                    # Garrafon se creo con el id 2
                    if det.producto.id == 2:
                        cant = det.cantidad + cant
        return cant

    def bolsas_vendidas(self):
        cant = 0
        # Importamos los modelos de pedidos
        from pedido.models import Pedido, Detalle
        for p in Pedido.objects.filter(fecha=self.fecha_a):
                for det in Detalle.objects.filter(pedido=p):
                    # Bolsas se creo con el id 3
                    if det.producto.id == 3:
                        cant = det.cantidad + cant
        return cant

    def es_primer(self):
        numero = None
        monto_c = None
        caudal_c = None
        ultimo = None
        n = self.pk-1
        if Venta.objects.filter(estado=0).exists():
            ultimo = Venta.objects.filter(pk=n).get()
            if ultimo.pk != self.pk:
                caudal_c = ultimo.caudal_c
                self.caudal_a = caudal_c
                if self.caudal_a != caudal_c:
                    raise ValidationError(
                        'El numero de apertura del caudal debe conicidir con el cierre')

    def id_aneterior(self):
        n = self.pk-1
        anterior = Venta.objects.filter(pk=n).get()
        return anterior.pk

    def __str__(self):
        return 'Monto: %s, Cuadal: %s, Fecha %s' % (self.saldo_c, self.caudal_c, self.fecha_a)

    def clean(self, **kwargs):
        super(Venta, self).clean()
        self.es_primer()

    def save(self):
        self.garrafones_vendidos()
        self.bolsas_vendidas()
        self.caudal_c = self.caudal_a + self.aumentar_caudalimetro()
        self.saldo_c = self.monto_vendido()
        super(Venta, self).save()