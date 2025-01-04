# forms.py
from django import forms
from .models import ResultadoPartido

class ResultadoPartidoForm(forms.ModelForm):
    class Meta:
        model = ResultadoPartido
        fields = ['equipo1', 'equipo2', 'resultado']
