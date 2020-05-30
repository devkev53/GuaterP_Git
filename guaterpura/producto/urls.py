from django.urls import path

from .views import ProducetoCreate, ProductoListView, ProductoUpdate, ProductoDelete

urlpatterns = [
	path('producto/new/', ProducetoCreate.as_view(), name='new_producto'),
	path('productos/', ProductoListView.as_view(), name='list_producto'),
	path('productos/edit/<int:pk>', ProductoUpdate.as_view(), name='update_producto'),
	path('productos/delete/<int:pk>', ProductoDelete.as_view(), name='delete_producto'),
]