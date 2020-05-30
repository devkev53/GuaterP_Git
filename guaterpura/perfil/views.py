from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.utils import timezone

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .models import Empleado, Puesto
from .forms import EmpleadoForm, PuestoForm

# Create your views here.

class EmpleadoCreate(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado:empelado_list')

class EmpleadoListView(ListView):

    model = Empleado
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoForm

class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleado:empelado_list')


''' --- PUESTO ---  '''
class PuestoCreate(CreateView):
    model = Puesto
    form_class = PuestoForm
    success_url = reverse_lazy('empleado:empelado_list')

class PuestoListView(ListView):

    model = Puesto
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PuestoUpdate(UpdateView):
    model = Puesto
    form_class = PuestoForm

class PuestoDelete(DeleteView):
    model = Puesto
    success_url = reverse_lazy('empleado:empelado_list')