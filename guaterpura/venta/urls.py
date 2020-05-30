from django.urls import path

from .views import crearVenta, finalizarVenta, ReporteVentasPDFView, ReporteVentasMesPDFView, ReporteVentasMesPDFView

urlpatterns = [
	path('crearVenta/', crearVenta, name='new_venta'),
	path('venta/finalizar/<int:id>', finalizarVenta, name='finalizar_venta'),
	path('reporteVentas/', ReporteVentasPDFView.as_view(), name='reporte_venta'),
	path('reporteVentas/Mes/', ReporteVentasMesPDFView.as_view(), name='reporte_mes'),
]