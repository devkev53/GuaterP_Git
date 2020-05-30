from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.utils import timezone
import datetime


from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from .models import Pedido, Detalle
from producto.models import Producto
from cliente.models import Cliente
from perfil.models import Empleado
from venta.models import Venta

from .forms import PedidoForm

# Create your views here.

def finalizarPedido(request, id):
	pedido = Pedido.objects.filter(pk=id)
	pedido.update(estado=True)

	return redirect('pedido:list_pedidos')

def pedidos(request, pedido_id=None):
	template_name = 'pedido/pedido_form.html'
	prod = Producto.objects.all()
	form_pedido = {}
	context = {}

	# Metodo Get
	if request.method=='GET':
		form_pedido = PedidoForm()
		print(pedido_id)
		ped = Pedido.objects.filter(pk=pedido_id).first()
		if ped:
			det = Detalle.objects.filter(pedido=ped)
			p = {
				'cliente': ped.cliente,
				'repartidor': ped.repartidor,
				'descuento': ped.descuento,
				'subtotal': ped.subtotal,
				'total': ped.total,
				'estado': ped.estado
			}
			form_pedido = PedidoForm(p)
		else:
			det = None
		context = {'productos': prod, 'pedido': ped, 'detalle': det, 'form_ped': form_pedido}

	# Metodo Post
	if request.method=='POST':
		cliente = request.POST.get("cliente")
		repartidor = request.POST.get("repartidor")
		descuento = request.POST.get("descuento")
		subtotal = request.POST.get("subtotal")
		total = request.POST.get("total")

		if not pedido_id:
			client = Cliente.objects.get(pk=cliente)
			rep = Empleado.objects.get(pk=repartidor)

			p = Pedido(
				cliente = client,
				repartidor = rep
				)

			if 	p:
				p.save()
				pedido_id=p.id
		else:
			p = Pedido.objects.filter(pk=pedido_id).first()
		if not pedido_id:
			return redirect('pedido:list_pedidos')

		producto = request.POST.get('prdoucto')
		cantidad = request.POST.get('cantidad')
		descuento = request.POST.get('descento')
		subtotal = request.POST.get('precio')
		total = request.POST.get('total')

		print(producto)

		prod = Producto.objects.get(pk=producto)

		det = Detalle(
				pedido = p,
				producto = prod,
				cantidad = cantidad,
				descuento = descuento,
				subtotal = subtotal,
				total = total
			)
		if det:
			det.save()

			sub_total = 0
			desc = 0

			print('Esta antes del for')
			for d in Detalle.objects.filter(pedido=pedido_id):
				sub_total = d.subtotal + sub_total
				desc = d.descuento + desc

			p.subtotal = sub_total
			print(sub_total)
			p.subtotal = desc
			print(desc)
			p.save()

		return redirect('pedido:pedido_edit', pedido_id=pedido_id)

	return render(request, template_name, context)


class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm

class PedidoListView(ListView):

    model = Pedido
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = datetime.date.today()
        venta = Venta.objects.filter(fecha_a=hoy)
        context['now'] = timezone.now()
        context['hoy'] = hoy
        context['venta_q'] = venta
        if venta.exists():
        	context['venta'] = venta.get()
        return context

class PedidoFinalizadoListView(ListView):
    model = Pedido
    paginate_by = 100
    template_name = 'pedido/pedido_finalizado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = datetime.date.today()
        venta = Venta.objects.filter(fecha_a=hoy)
        context['now'] = timezone.now()
        context['hoy'] = hoy
        context['venta_q'] = venta
        if venta.exists():
        	context['venta'] = venta.get()
        return context

class DetallePedidoDelete(DeleteView):
    model = Detalle

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
    	pedido_id = self.kwargs['pedido_id']
    	return reverse_lazy('pedido:pedido_edit', kwargs={'pedido_id':pedido_id})