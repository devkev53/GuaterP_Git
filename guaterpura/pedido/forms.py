from django.forms import ModelForm
from django import forms

from .models import Pedido, Detalle

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'repartidor', 'subtotal', 'descuento', 'total']
        widgets={
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'repartidor': forms.Select(attrs={'class':'form-control'}),
            'descuento': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Descuento', 'readonly':True}),
            'subtotal': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Subtotal', 'readonly':True}),
            'total': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Monto del Pedido', 'readonly':True}),
        }