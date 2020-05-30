from django.contrib import admin

from .models import Pedido, Detalle

# Register your models here.

class DetalleInline(admin.TabularInline):
    model = Detalle
    min_num = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetalleInline,]
    list_display = ['fecha', 'cliente', 'repartidor', 'subtotal', 'total']


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Detalle)