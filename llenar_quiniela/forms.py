# forms.py
from django import forms
from .models import EquiposPartidos

class EquiposPartidoForm(forms.ModelForm):
    class Meta:
        model = EquiposPartidos
        fields = ['j', 'eq1', 'eq2']
