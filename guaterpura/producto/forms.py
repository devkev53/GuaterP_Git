from django.forms import ModelForm
from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        labels={
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre del Producto'}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Precio del Producto'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Descripcion', 'rows':'3'}),
        }