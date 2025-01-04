from django.shortcuts import render
from .models import Jornadas

# Create your views here.

def tabla_general(request):
    # Obtener todas las instancias de Jornada ordenadas por la suma
    jornadas = Jornadas.objects.all().order_by('-suma_j', 'suma_j_c')

    # Pasar las jornadas al template
    return render(request, 'tabla_general/tabla_general.html', {'jornadas': jornadas, 'page':'tabla_general'})
