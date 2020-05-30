from django.contrib import admin

from .models import Puesto, Empleado

# Register your models here.

admin.site.register(Puesto)
admin.site.register(Empleado)