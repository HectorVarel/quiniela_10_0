from django.shortcuts import render, HttpResponse
from tabla_general.models import Jornadas
from .models import Fotos_portada

# Create your views here.

def principal(request):
    jornadas = Jornadas.objects.all().order_by('-suma_j').first()
    fotos_por = Fotos_portada.objects.all()
    dicc_desc = []
    dicc_podium = []
    dicc_hist = []

    for i in fotos_por:
        dicc_desc.append({
            "desc": i.descenso
        })
        dicc_podium.append({
            "desc": i.podium
        })
        dicc_hist.append({
            "desc": i.historico
        })
    #print(jornadas)

    return render(request, 'principal/principal copy.html', {'podium': dicc_podium, 'desc': dicc_desc, 'hist': dicc_hist})
