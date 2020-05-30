from django.urls import path

from .views import EmpleadoCreate, EmpleadoListView, EmpleadoUpdate, EmpleadoDelete, \
PuestoCreate, PuestoUpdate, PuestoDelete, PuestoListView

urlpatterns = [
	path('empleados/', EmpleadoListView.as_view(), name='empelado_list'),
	path('empleados/nuevo/', EmpleadoCreate.as_view(), name='add_empleado'),
	path('empleados/edit/<int:pk>', EmpleadoUpdate.as_view(), name='update_empleado'),
	path('empleados/delete/<int:pk>', EmpleadoDelete.as_view(), name='delete_empleado'),
	# Puestos
	path('puestos/', PuestoListView.as_view(), name='puesto_list'),
	path('puestos/nuevo/', PuestoCreate.as_view(), name='add_puesto'),
	path('puestos/edit/<int:pk>', PuestoUpdate.as_view(), name='update_puesto'),
	path('puestos/delete/<int:pk>', PuestoDelete.as_view(), name='delete_puesto'),
]