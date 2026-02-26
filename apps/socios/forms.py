from django import forms
from .models import Socio


def clean(self):
    cleaned_data = super().clean()
    tipo = cleaned_data.get("tipo")
    condicion = cleaned_data.get("condicion")

    if tipo and tipo.nombre.lower() != "adulto" and condicion:
        self.add_error("condicion", "Solo los adultos pueden tener condición.")

    return cleaned_data

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['numero_festero', 'nombre', 'apellidos', 'dni', 'email', 'telefono','tipo', 'condicion', 'estado']
        widgets = {
            'numero_festero': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'condicion': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
