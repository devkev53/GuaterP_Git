from django.forms import ModelForm
from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        labels={
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre del Cliente'}),
            'direccion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Direccion del Cliente', 'rows':'3'}),
            'nit': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'NIT del Cliente', 'maxlength':'9'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Telefono del Cliente', 'maxlength':'9'}),
            'tipo_cliente': forms.Select(attrs={'class':'form-control', 'placeholder': 'Tipo de Cliente'}),
        }