from django.forms import ModelForm
from django import forms

from .models import Empleado, Puesto

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        labels={
        }
        widgets={
            'puesto': forms.Select(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellidos'}),
            'dpi': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'No. de DPI'}),
            'nit': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'No. de NIT'}),
            'fechaNacimiento': forms.DateInput(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Direccion', 'rows':'3'}),
        }

class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'
        labels={
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombres del Puesto'}),
            'salario': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Salario'}),
        }