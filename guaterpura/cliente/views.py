from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.utils import timezone

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .models import Cliente

from .forms import ClienteForm

# Create your views here.

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:list_cliente')

class ClienteListView(ListView):
    model = Cliente
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:list_cliente')

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente:list_cliente')