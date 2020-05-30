from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.utils import timezone

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .models import Producto

from .forms import ProductoForm

# Create your views here.

class ProducetoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:list_producto')

class ProductoListView(ListView):

    model = Producto
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:list_producto')

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto:list_producto')

