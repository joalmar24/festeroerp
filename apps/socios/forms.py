from django import forms
from .models import Socio, Condicion


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Por defecto NO hay condiciones
        self.fields['condicion'].queryset = Condicion.objects.none()
        self.fields['condicion'].help_text = (
            "Seleccione primero un Tipo y guarde para cargar las condiciones."
        )
        # EL STYLE
        if self.fields['condicion'].disabled:
            self.fields['condicion'].widget.attrs['style'] = 'background:#eee;'

        # --- EDITANDO socio existente ---
        if self.instance.pk and self.instance.tipo:
            self.fields['condicion'].queryset = Condicion.objects.filter(
                tipo=self.instance.tipo
            )
            self.fields['condicion'].disabled = False
            self.fields['condicion'].help_text = ""

        # --- POST (cuando cambias tipo) ---
        if 'tipo' in self.data:
            try:
                tipo_id = int(self.data.get('tipo'))
                self.fields['condicion'].queryset = Condicion.objects.filter(
                    tipo_id=tipo_id
                )
                self.fields['condicion'].disabled = False
                self.fields['condicion'].help_text = ""
            except:
                pass


#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs) 

       # si ya hay tipo seleccionado, filtramos condiciones
#        if 'tipo' in self.data:
#            try:
#                tipo_id = int(self.data.get('tipo'))
#                self.fields['condicion'].queryset = Condicion.objects.filter(tipo_id=tipo_id)
#            except:
#                pass
#        elif self.instance.pk and self.instance.tipo:
#            self.fields['condicion'].queryset = self.instance.tipo.condiciones.all()
#        else:
#            self.fields['condicion'].queryset = Condicion.objects.none()