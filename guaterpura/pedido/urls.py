from django.urls import path

from .views import PedidoListView, PedidoCreate, pedidos, DetallePedidoDelete, finalizarPedido, PedidoFinalizadoListView

urlpatterns = [
	path('pedidos/', PedidoListView.as_view(), name='list_pedidos'),
	path('pedidos/finalizados/', PedidoFinalizadoListView.as_view(), name='list_pedidos_fin'),
	path('pedidos/new/', pedidos, name='new_pedido'),
	path('pedidos/edit/<int:pedido_id>', pedidos, name='pedido_edit'),
	path('pedidos/finalizar/<int:id>', finalizarPedido, name='finalizar_pedido'),

	path('pedidos/edit/<int:pedido_id>/delete/<int:pk>', DetallePedidoDelete.as_view(), name='detalle_delete'),
]