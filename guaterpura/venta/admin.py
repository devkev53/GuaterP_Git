from django.contrib import admin

from .models import Venta

# Register your models here.

class VentaAdmin(admin.ModelAdmin):
    list_display = ['fecha_a', 'estado', 'saldo_a', 'saldo_c', 'caudal_a', 'caudal_c', 'aumentar_caudalimetro']

admin.site.register(Venta, VentaAdmin)