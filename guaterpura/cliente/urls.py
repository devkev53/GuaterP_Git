from django.urls import path

from .views import ClienteCreate, ClienteDelete, ClienteUpdate, ClienteListView

urlpatterns = [
	path('cliente/new/', ClienteCreate.as_view(), name='new_cliente'),
	path('clientes/', ClienteListView.as_view(), name='list_cliente'),
	path('clientes/edit/<int:pk>', ClienteUpdate.as_view(), name='update_cliente'),
	path('clientes/delete/<int:pk>', ClienteDelete.as_view(), name='delete_cliente'),
]