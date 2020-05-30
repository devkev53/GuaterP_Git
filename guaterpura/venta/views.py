from django.shortcuts import render, redirect

from django.utils import timezone
import datetime

from easy_pdf.views import PDFTemplateView

from .models import Venta
from pedido.models import Pedido, Detalle

# Create your views here.

def crearVenta(request):
    venta = Venta.objects.last()
    hoy = datetime.date.today()
    hora = timezone.now().time()

    if venta:
        v = Venta(
            fecha_a = hoy,
            fecha_c = hoy,
            hora_a = hora,
            hora_c = hora,
            estado = 1,
            saldo_a = venta.saldo_a,
            saldo_c = venta.saldo_c,
            caudal_a = venta.caudal_c,
            caudal_c = venta.aumentar_caudalimetro()
        )

    else:
        v = Venta(
            fecha_a = hoy,
            fecha_c = hoy,
            hora_a = hora,
            hora_c = hora,
            estado = 1,
            saldo_a = 0,
            saldo_c = 0,
            caudal_a = 0,
            caudal_c = 0
        )

        v.save()
    return redirect('pedido:list_pedidos')


def finalizarVenta(request, id):
    venta = Venta.objects.filter(pk=id)
    venta.update(estado=0)
    venta.get().save()

    return redirect('pedido:list_pedidos')


class ReporteVentasPDFView(PDFTemplateView ):
    template_name  =  'venta/registro_ventas.html'

    def get_context_data(self, **kwargs):
        hoy = datetime.date.today()
        pedidos = Pedido.objects.filter(fecha=hoy)
        detalles = Detalle.objects.filter(pedido__fecha=hoy)
        venta = Venta.objects.filter(fecha_a=hoy).get()

        return super(ReporteVentasPDFView, self).get_context_data(
            pagesize='Legal landscape',
            title='RegistroVentas',
            pedidos=pedidos,
            detalles=detalles,
            venta=venta,
            hoy=hoy,
            **kwargs
            )

class ReporteVentasMesPDFView(PDFTemplateView ):
    template_name  =  'venta/reporte_mes.html'

    def get_context_data(self, **kwargs):
        ano = datetime.datetime.today().year
        mes = datetime.datetime.today().month
        fecha_in = (str(ano)+"-"+str(mes)+'-'+'01')
        fecha_fin = (str(ano)+"-"+str(mes)+'-'+'31')
        hoy = datetime.date.today()
        pedidos = Pedido.objects.filter(fecha__range=(fecha_in, fecha_fin))
        detalles = Detalle.objects.filter(pedido__fecha__range=(fecha_in, fecha_fin))
        v = Venta.objects.filter(fecha_a__range=(fecha_in, fecha_fin))
        t = 0
        for p in pedidos:
            dato = p.total
            t = p.total + float(t)

        '''g = 0
        b = 0
        first = v.first()
        last = v.last()

        for dato in v:
            g = dato.garrafones_vendidos() + g
            b = dato.bolsas_vendidas() + b

        venta = {
            'm_i':first.caudal_a.first(),
            'm_f': last.caudal_c.last(),
            'c_i': first.caudal_a.first(),
            'c_f': last.caudal_c.last(),
            'g': g,
            'b': b
        }'''


        return super(ReporteVentasMesPDFView, self).get_context_data(
            pagesize='Legal landscape',
            title='RegistroVentas',
            pedidos=pedidos,
            detalles=detalles,
            venta=v,
            total_venta=t,
            hoy=hoy,
            **kwargs
            )