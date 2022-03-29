from django import forms
from .models import Contacto, Direccion, Telefono

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def valida_nombre(value):
    if len(value) > 60 or len(value) < 2:
        raise ValidationError(
            _('Longitud maxima de 60 y minima de 2'),
            params={'value': value},
        )
    if not re.match(r"^[A-Za-zÀ-ÿ& \s]{2,60}$", value):
        raise ValidationError(
            _('Solo usa letras y espacios'),
            params={'value': value},
        )

def valida_numero(value):
    if not re.match(r"^[0-9]{1,10}$", value):
        raise ValidationError(
            _('Especifica en números'),
            params={'value': value},
        )

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(validators=[valida_nombre])
    apellidos = forms.CharField(validators=[valida_nombre])
    class Meta:
        model = Contacto
        fields = ('nombre', 'apellidos', 'fecha_nacio', 'fotografia')
        labels = {
            'fecha_nacio': ('Fecha de nacimiento'),
            'nombre': ('Nombre'),
            'apellidos': ('Apellidos')
        }
        widgets = {
            'fecha_nacio': forms.SelectDateWidget( empty_label=("Año", "Mes", "Día"), years=[x for x in reversed(range(1900, 2025))], attrs={'style': 'padding:5px 10px; margin:5px 5px'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'fotografia': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class DireccionForm(forms.ModelForm):
    numero_exterior = forms.CharField(validators=[valida_numero])
    numero_interior = forms.CharField(validators=[valida_numero])
    class Meta:
        model = Direccion
        fields = ("calle", "numero_exterior", "numero_interior", "colonia", "municipio", "estado", "referencias")
        labels = {   
            'calle': ('Calle'), 
            'numero_exterior': ('Número exterior'), 
            'numero_interior': ('Número interior'), 
            'colonia': ('Colonia'), 
            'municipio': ('Municipio'), 
            'estado': ('Estado'),   
            'referencias': ('Referencias'), 
        }
        widgets = {
            'calle': forms.TextInput(),
            'colonia': forms.TextInput(),
            'munici[io': forms.TextInput(),
        }

class TelefonoForm(forms.ModelForm):
    numero = forms.CharField(validators=[valida_numero])
    class Meta:
        model = Telefono
        fields = ('tipo', 'alias', 'numero')