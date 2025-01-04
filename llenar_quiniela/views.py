# views.py
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.conf import settings
from .forms import EquiposPartidoForm
from .models import Prediccion, Fotos_quiniela
from tabla_general.models import Cartas, Num_quiniela, Cartas_aux, jugadores_gol, Equipos
from llenar_quiniela.models import imagenes_cartas, Equipos_gol, Equipos_fotos, Juegos_pendientes, Equipos_tiempo, Momios
import os
import unicodedata

def obtener_momios(nj):
    jornada = f'j{nj}'
    
    # Obtener el objeto de jugadores_gol
    momios = Momios.objects.first()
    print("SI")
    if momios:
        mom = getattr(momios, jornada).split(" ")
        print(mom)
        dicc = []
        dicc.append({
            'mom1': mom[0],
            'mom2': mom[1],
            'mom3': mom[2],
            })
        #print(dicc)
    return dicc
def quitar_mayusculas_y_acentos(palabra):
    
    if palabra == 'San Luis':
        palabra_sin_acentos = 'san_luis'
    elif palabra == 'Cruz azul':
        palabra_sin_acentos = 'cruz_azul'
    else:
        # Convertir la palabra a minúsculas
        palabra = palabra.lower()
        # Eliminar los acentos
        palabra_sin_acentos = ''.join((c for c in unicodedata.normalize('NFD', palabra) if unicodedata.category(c) != 'Mn'))
    return palabra_sin_acentos

def obtener_equipos_disponibles(nombre):
    equipos = ['atlas', 'america', 'chivas', 'cruz_azul', 'tijuana', 'puebla', 'queretaro', 'pumas', 'toluca', 'santos',
               'monterrey', 'tigres', 'mazatlan', 'necaxa', 'san_luis', 'leon', 'juarez', 'pachuca']
    dicc_equipos = []
    dicc_equipos.append({
        'equipo':'-- Selecciona --',
    })
    registros = Equipos_gol.objects.filter(nombre=nombre).values_list()
    for reg in registros:
        for i, r in enumerate(reg):
            if i != 0 and i != 1:
                #print(i)
                if r == '1':
                    #print("ENTRO")
                    #print(equipos[i-2])
                    dicc_equipos.append({
                        'equipo': equipos[i-2],
                    })
                    #print("SALIO")
    #print(dicc_equipos)
    return dicc_equipos

def obtener_equipos_disponibles_tiempo(nombre):
    equipos = ['atlas', 'america', 'chivas', 'cruz_azul', 'tijuana', 'puebla', 'queretaro', 'pumas', 'toluca', 'santos',
               'monterrey', 'tigres', 'mazatlan', 'necaxa', 'san_luis', 'leon', 'juarez', 'pachuca']
    dicc_equipos = []
    dicc_equipos.append({
        'equipo':'-- Selecciona --',
    })
    registros = Equipos_tiempo.objects.filter(nombre=nombre).values_list()
    for reg in registros:
        for i, r in enumerate(reg):
            if i != 0 and i != 1:
                #print(i)
                if r == '1':
                    #print("ENTRO")
                    #print(equipos[i-2])
                    dicc_equipos.append({
                        'equipo': equipos[i-2],
                    })
                    #print("SALIO")
    
    return dicc_equipos

def jugadores_disponibles_robo(nj, num_jor):
    registros = Prediccion.objects.all()
    #print('Jugadores Disponibles')
    nombres = []
    for r in registros:
        if r.nombre != 'Resultados':
            conteo_X = getattr(r, nj).split(', ').count('X')
            conteo_XX = getattr(r, nj).split(', ').count('XX')
            conteo_00 = getattr(r, nj).split(', ').count('0-0')
            if conteo_X == 11 or conteo_XX == 11 or conteo_00 == 11:
                nombres.append(r.nombre)
    #print(nombres)
    diccio = []
    diccio.append({
        'nombre': '-- Selecciona --',
        'carta': 'NC',
    })
    for nom in nombres:
        registros = Cartas.objects.filter(nombre=nom).values_list()
        #print(registros)
        for r in registros:
            cad = ', '.join(map(str, r))
            cad = cad.split(', ')
            #print(cad[num_jor + 1])
            diccio.append({
                'nombre': nom,
                'carta': cad[num_jor + 1],
            })
    diccio.append({
        'nombre': 'No hay cartas',
        'carta': 'NC',
    })
    return diccio

def ingresar_resultado(request):
    # MOMIOS
    
    # Obtener todos los registros de la base de datos
    registros = Fotos_quiniela.objects.all()
    #print(registros)
    
    reg_car = Cartas.objects.all()
    reg_im_car = imagenes_cartas.objects.all()
    reg_jueg_pen = Juegos_pendientes.objects.all()
    datos_procesados = []
    datos_procesados2 = []
    
    reg_q = Num_quiniela.objects.all()
    
    for r in reg_q:
        numero_jornada = int(r.num_jor)
    
    momios = obtener_momios(numero_jornada)
    
    nombre_campo = f'j{numero_jornada}'
    num_campo_robo_carta = f'pJ{numero_jornada}'
    #print(nombre_campo)
    
    for registro in reg_car:
        datos_procesados.append({
            'nombre': registro.nombre,
            'carta': getattr(registro, nombre_campo),
        })
    datos_procesados.append({
            'nombre': 'Seleccione',
            'carta': 'NC',
        })
    for registro in registros:
        #print(type(nombre_campo))
        datos_procesados2.append({
            'jornada': getattr(registro, nombre_campo),
        })
    jueg_pen = []
    
    for registro in reg_jueg_pen:
        secuencia = [item.strip() for item in getattr(registro, nombre_campo).split(',')]
        for jp in secuencia:
            jueg_pen.append({
                'nombre': jp,
            })
    #print("JUEGOS PENDIENTES")
    #print(jueg_pen)
    #print(datos_procesados2)
    if request.method == 'POST':
        if 'cartas' in request.POST:
            jor = request.POST['cartas']
            jor = jor.split(' ')
            if len(jor) == 3:
                if jor[0] == 'Luis':
                    nom = 'Luis Angel'
                else:
                    nom = 'Juan Luis'
                car = jor[2]
            else:
                nom = jor[0]
                car = jor[1]
            #print(nom, car)
            if nom != 'Seleccione':
                equipos_disponibles_gol = obtener_equipos_disponibles(nom)
                equipos_disponibles_tiempo = obtener_equipos_disponibles(nom)
                equipos_disponibles_multi = obtener_equipos_disponibles(nom)
            if car == 'RC':
                dicc_robo = jugadores_disponibles_robo(num_campo_robo_carta, numero_jornada)
                #jugador_atr = request.POST['robo_carta']
                #print(jugador_atr)
            else:
                dicc_robo = []
        else:
            nom = 'Seleccione'
            car = 'NC'
            equipos_disponibles_gol = []
            equipos_disponibles_tiempo = []
            equipos_disponibles_multi = []
            dicc_robo = []
            aux = 0
        if 'nombre_j' in request.POST:
            if 'partido1' in request.POST and  'partido2' in request.POST and 'partido3' in request.POST and 'partido4' in request.POST and 'partido5' in request.POST and 'partido6' in request.POST and 'partido7' in request.POST and 'partido8' in request.POST and 'partido9' in request.POST and 'partido10' in request.POST and 'partido11' in request.POST:
                partido1 = request.POST['partido1']
                partido2 = request.POST['partido2']
                partido3 = request.POST['partido3']
                partido4 = request.POST['partido4']
                partido5 = request.POST['partido5']
                partido6 = request.POST['partido6']
                partido7 = request.POST['partido7']
                partido8 = request.POST['partido8']
                partido9 = request.POST['partido9']
                partido10 = request.POST['partido10']
                partido11 = request.POST['partido11']
                nombre_j = request.POST['nombre_j']
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                
                sec = partido1 + ', ' + partido2 + ', ' + partido3 + ', ' + partido4 + ', ' + partido5 + ', ' + partido6 + ', ' + partido7 + ', ' + partido8 + ', ' + partido9 + ', ' + partido10 + ', ' + partido11
                #print(sec)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()
                print('NC, IQ --------- Disponibles')
                
            elif 'partido1CH' in request.POST and  'partido2CH' in request.POST and 'partido3CH' in request.POST and 'partido4CH' in request.POST and 'partido5CH' in request.POST and 'partido6CH' in request.POST and 'partido7CH' in request.POST and 'partido8CH' in request.POST and 'partido9CH' in request.POST and 'partido10CH' in request.POST and 'partido11CH' in request.POST:
                partido1 = request.POST.getlist('partido1CH')
                partido1 = ''.join(partido1)
                partido2 = request.POST.getlist('partido2CH')
                partido2 = ''.join(partido2)
                partido3 = request.POST.getlist('partido3CH')
                partido3 = ''.join(partido3)
                partido4 = request.POST.getlist('partido4CH')
                partido4 = ''.join(partido4)
                partido5 = request.POST.getlist('partido5CH')
                partido5 = ''.join(partido5)
                partido6 = request.POST.getlist('partido6CH')
                partido6 = ''.join(partido6)
                partido7 = request.POST.getlist('partido7CH')
                partido7 = ''.join(partido7)
                partido8 = request.POST.getlist('partido8CH')
                partido8 = ''.join(partido8)
                partido9 = request.POST.getlist('partido9CH')
                partido9 = ''.join(partido9)
                partido10 = request.POST.getlist('partido10CH')
                partido10 = ''.join(partido10)
                partido11 = request.POST.getlist('partido11CH')
                partido11 = ''.join(partido11)
                
                sec = partido1 + ', ' + partido2 + ', ' + partido3 + ', ' + partido4 + ', ' + partido5 + ', ' + partido6 + ', ' + partido7 + ', ' + partido8 + ', ' + partido9 + ', ' + partido10 + ', ' + partido11
                
                nombre_j = request.POST['nombre_j']
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                #print(sec, nombre_j)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()
                
                
                #print('OD, OT --------- Disponibles')
            
            elif 'partido1LMA' in request.POST and  'partido2LMA' in request.POST and 'partido3LMA' in request.POST and 'partido4LMA' in request.POST and 'partido5LMA' in request.POST and 'partido6LMA' in request.POST and 'partido7LMA' in request.POST and 'partido8LMA' in request.POST and 'partido9LMA' in request.POST and 'partido10LMA' in request.POST and 'partido11LMA' in request.POST and 'partido1VMA' in request.POST and  'partido2VMA' in request.POST and 'partido3VMA' in request.POST and 'partido4VMA' in request.POST and 'partido5VMA' in request.POST and 'partido6VMA' in request.POST and 'partido7VMA' in request.POST and 'partido8VMA' in request.POST and 'partido9VMA' in request.POST and 'partido10VMA' in request.POST and 'partido11VMA' in request.POST:
                # Obtener los valores ingresados por los participantes
                partido1L = request.POST.get('partido1LMA')
                partido1V = request.POST.get('partido1VMA')
                partido1 = str(partido1L) + '-' + str(partido1V)
                partido2L = request.POST.get('partido2LMA')
                partido2V = request.POST.get('partido2VMA')
                partido2 = str(partido2L) + '-' + str(partido2V)
                partido3L = request.POST.get('partido3LMA')
                partido3V = request.POST.get('partido3VMA')
                partido3 = str(partido3L) + '-' + str(partido3V)
                partido4L = request.POST.get('partido4LMA')
                partido4V = request.POST.get('partido4VMA')
                partido4 = str(partido4L) + '-' + str(partido4V)
                partido5L = request.POST.get('partido5LMA')
                partido5V = request.POST.get('partido5VMA')
                partido5 = str(partido5L) + '-' + str(partido5V)
                partido6L = request.POST.get('partido6LMA')
                partido6V = request.POST.get('partido6VMA')
                partido6 = str(partido6L) + '-' + str(partido6V)
                partido7L = request.POST.get('partido7LMA')
                partido7V = request.POST.get('partido7VMA')
                partido7 = str(partido7L) + '-' + str(partido7V)
                partido8L = request.POST.get('partido8LMA')
                partido8V = request.POST.get('partido8VMA')
                partido8 = str(partido8L) + '-' + str(partido8V)
                partido9L = request.POST.get('partido9LMA')
                partido9V = request.POST.get('partido9VMA')
                partido9 = str(partido9L) + '-' + str(partido9V)
                partido10L = request.POST.get('partido10LMA')
                partido10V = request.POST.get('partido10VMA')
                partido10 = str(partido10L) + '-' + str(partido10V)
                partido11L = request.POST.get('partido11LMA')
                partido11V = request.POST.get('partido11VMA')
                partido11 = str(partido11L) + '-' + str(partido11V)
                nombre_j = request.POST['nombre_j']
                sec = partido1 + ', ' + partido2 + ', ' + partido3 + ', ' + partido4 + ', ' + partido5 + ', ' + partido6 + ', ' + partido7 + ', ' + partido8 + ', ' + partido9 + ', ' + partido10 + ', ' + partido11
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                #print(sec, nombre_j)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()
                #print(sec)
                #print('MA --------- Disponibles')
                
            elif 'partido1M' in request.POST and  'partido2M' in request.POST and 'partido3M' in request.POST and 'partido4M' in request.POST and 'partido5M' in request.POST and 'partido6M' in request.POST and 'partido7M' in request.POST and 'partido8M' in request.POST and 'partido9M' in request.POST and 'partido10M' in request.POST and 'partido11M' in request.POST:
                partido1 = request.POST['partido1M']
                partido2 = request.POST['partido2M']
                partido3 = request.POST['partido3M']
                partido4 = request.POST['partido4M']
                partido5 = request.POST['partido5M']
                partido6 = request.POST['partido6M']
                partido7 = request.POST['partido7M']
                partido8 = request.POST['partido8M']
                partido9 = request.POST['partido9M']
                partido10 = request.POST['partido10M']
                partido11 = request.POST['partido11M']
                nombre_j = request.POST['nombre_j']
                eq_sel = request.POST['equipo_seleccionadoM']
                sec = partido1 + ', ' + partido2 + ', ' + partido3 + ', ' + partido4 + ', ' + partido5 + ', ' + partido6 + ', ' + partido7 + ', ' + partido8 + ', ' + partido9 + ', ' + partido10 + ', ' + partido11
                #multi = request.POST['multi']
                #m = str(int(multi)-1)
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                print("EQUIPO SELECCIONADO: ", eq_sel)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()

                objeto = get_object_or_404(Cartas_aux, nombre=nombre_j)
                nombre_campo = f'j{numero_jornada}'
                setattr(objeto, nombre_campo, str(eq_sel))
                objeto.save()

                objeto = get_object_or_404(Equipos_gol, nombre=nombre_j)
                #print(objeto)
                setattr(objeto, eq_sel, '0')
                objeto.save()

                #print(sec, m)
                nombre_j = request.POST['nombre_j']
                #print('M --------- Disponibles')

            elif 'partido1J' in request.POST and  'partido2J' in request.POST and 'partido3J' in request.POST and 'partido4J' in request.POST and 'partido5J' in request.POST and 'partido6J' in request.POST and 'partido7J' in request.POST and 'partido8J' in request.POST and 'partido9J' in request.POST and 'partido10J' in request.POST and 'partido11J' in request.POST:
                partido1 = request.POST['partido1J']
                partido2 = request.POST['partido2J']
                partido3 = request.POST['partido3J']
                partido4 = request.POST['partido4J']
                partido5 = request.POST['partido5J']
                partido6 = request.POST['partido6J']
                partido7 = request.POST['partido7J']
                partido8 = request.POST['partido8J']
                partido9 = request.POST['partido9J']
                partido10 = request.POST['partido10J']
                partido11 = request.POST['partido11J']
                jug1 = request.POST['jug'] 
                jug2 = request.POST['jug2']
                eq_sel = request.POST['equipo_seleccionado']
                jug = jug1 + " " + jug2 + " " + eq_sel
                nombre_j = request.POST['nombre_j']
                sec = partido1 + ', ' + partido2 + ', ' + partido3 + ', ' + partido4 + ', ' + partido5 + ', ' + partido6 + ', ' + partido7 + ', ' + partido8 + ', ' + partido9 + ', ' + partido10 + ', ' + partido11
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                #print(sec, nombre_j, eq_sel)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()
                #print("predicciones")
                objeto = get_object_or_404(Cartas_aux, nombre=nombre_j)
                print(objeto)
                nombre_campo = f'j{numero_jornada}'
                setattr(objeto, nombre_campo, jug)
                objeto.save()
                #print("jugador")
                objeto = get_object_or_404(Equipos_gol, nombre=nombre_j)
                print(objeto)
                setattr(objeto, eq_sel, '0')
                objeto.save()
                #print("equipos")
                
                #print('J --------- Disponibles')
            elif 'partido1T' in request.POST and  'partido2T' in request.POST and 'partido3T' in request.POST and 'partido4T' in request.POST and 'partido5T' in request.POST and 'partido6T' in request.POST and 'partido7T' in request.POST and 'partido8T' in request.POST and 'partido9T' in request.POST and 'partido10T' in request.POST and 'partido11T' in request.POST:
                partido1 = request.POST['partido1T']
                partido2 = request.POST['partido2T']
                partido3 = request.POST['partido3T']
                partido4 = request.POST['partido4T']
                partido5 = request.POST['partido5T']
                partido6 = request.POST['partido6T']
                partido7 = request.POST['partido7T']
                partido8 = request.POST['partido8T']
                partido9 = request.POST['partido9T']
                partido10 = request.POST['partido10T']
                partido11 = request.POST['partido11T']
                jug = request.POST['tiempo_gol_inicio']
                jug2 = request.POST['tiempo_gol_final']
                eq_sel = request.POST['equipo_seleccionado']
                jug = jug + "-" + jug2 + ":" + eq_sel
                nombre_j = request.POST['nombre_j']
                sec = partido1 + ', ' + partido2 + ', ' + partido3 + ', ' + partido4 + ', ' + partido5 + ', ' + partido6 + ', ' + partido7 + ', ' + partido8 + ', ' + partido9 + ', ' + partido10 + ', ' + partido11
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                #print(sec, nombre_j)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()
                #print("predicciones")
                objeto = get_object_or_404(Cartas_aux, nombre=nombre_j)
                #print(objeto)
                nombre_campo = f'j{numero_jornada}'
                setattr(objeto, nombre_campo, jug)
                objeto.save()
                #print("jugador")
                objeto = get_object_or_404(Equipos_gol, nombre=nombre_j)
                #print(objeto)
                setattr(objeto, eq_sel, '0')
                objeto.save()
                #print("equipos")
                
                #print('J --------- Disponibles')
            elif 'partido1DQ1' in request.POST and  'partido2DQ1' in request.POST and 'partido3DQ1' in request.POST and 'partido4DQ1' in request.POST and 'partido5DQ1' in request.POST and 'partido6DQ1' in request.POST and 'partido7DQ1' in request.POST and 'partido8DQ1' in request.POST and 'partido9DQ1' in request.POST and 'partido10DQ1' in request.POST and 'partido11DQ1' in request.POST and 'partido1DQ2' in request.POST and  'partido2DQ2' in request.POST and 'partido3DQ2' in request.POST and 'partido4DQ2' in request.POST and 'partido5DQ2' in request.POST and 'partido6DQ2' in request.POST and 'partido7DQ2' in request.POST and 'partido8DQ2' in request.POST and 'partido9DQ2' in request.POST and 'partido10DQ2' in request.POST and 'partido11DQ2' in request.POST:
                
                partido1DQ1 = request.POST['partido1DQ1']
                partido2DQ1 = request.POST['partido2DQ1']
                partido3DQ1 = request.POST['partido3DQ1']
                partido4DQ1 = request.POST['partido4DQ1']
                partido5DQ1 = request.POST['partido5DQ1']
                partido6DQ1 = request.POST['partido6DQ1']
                partido7DQ1 = request.POST['partido7DQ1']
                partido8DQ1 = request.POST['partido8DQ1']
                partido9DQ1 = request.POST['partido9DQ1']
                partido10DQ1 = request.POST['partido10DQ1']
                partido11DQ1 = request.POST['partido11DQ1']

                partido1DQ2 = request.POST['partido1DQ2']
                partido2DQ2 = request.POST['partido2DQ2']
                partido3DQ2 = request.POST['partido3DQ2']
                partido4DQ2 = request.POST['partido4DQ2']
                partido5DQ2 = request.POST['partido5DQ2']
                partido6DQ2 = request.POST['partido6DQ2']
                partido7DQ2 = request.POST['partido7DQ2']
                partido8DQ2 = request.POST['partido8DQ2']
                partido9DQ2 = request.POST['partido9DQ2']
                partido10DQ2 = request.POST['partido10DQ2']
                partido11DQ2 = request.POST['partido11DQ2']

                nombre_j = request.POST['nombre_j']

                sec = partido1DQ1 + partido1DQ2 + ', ' + partido2DQ1 + partido2DQ2 + ', ' + partido3DQ1 + partido3DQ2 + ', ' + partido4DQ1 + partido4DQ2 + ', ' + partido5DQ1 + partido5DQ2 + ', ' + partido6DQ1 + partido6DQ2 + ', ' + partido7DQ1 + partido7DQ2 + ', ' + partido8DQ1 + partido8DQ2 + ', ' + partido9DQ1 + partido9DQ2 + ', ' + partido10DQ1 + partido10DQ2 + ', ' + partido11DQ1 + partido11DQ2
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                #print(sec, nombre_j)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()
                #print(sec)
                nombre_j = request.POST['nombre_j']
                
                #print('DQ --------- Disponibles')
            elif 'partido1E' in request.POST and  'partido2E' in request.POST and 'partido3E' in request.POST and 'partido4E' in request.POST and 'partido5E' in request.POST and 'partido6E' in request.POST and 'partido7E' in request.POST and 'partido8E' in request.POST and 'partido9E' in request.POST and 'partido10E' in request.POST and 'partido11E' in request.POST:
                
                partido1 = request.POST['partido1E']
                partido2 = request.POST['partido2E']
                partido3 = request.POST['partido3E']
                partido4 = request.POST['partido4E']
                partido5 = request.POST['partido5E']
                partido6 = request.POST['partido6E']
                partido7 = request.POST['partido7E']
                partido8 = request.POST['partido8E']
                partido9 = request.POST['partido9E']
                partido10 = request.POST['partido10E']
                partido11 = request.POST['partido11E']
                nombre_j = request.POST['nombre_j']
                eq_sel = request.POST['equipo_seleccionado']
                
                oe1 = request.POST['OE1']
                #print("SI")
                oe2 = request.POST['OE2']
                oe3 = request.POST['OE3']
                auxiliar = oe1 + " " + oe2 + " " + oe3 + " " + eq_sel
                sec = partido1 + ', ' + partido2 + ', ' + partido3 + ', ' + partido4 + ', ' + partido5 + ', ' + partido6 + ', ' + partido7 + ', ' + partido8 + ', ' + partido9 + ', ' + partido10 + ', ' + partido11
                
                nombre_j = request.POST['nombre_j']
                if nombre_j == 'Luis':
                    nombre_j = 'Luis Angel'
                elif nombre_j == 'Juan':
                    nombre_j = 'Juan Luis'
                #print(sec, nombre_j)
                objeto = get_object_or_404(Prediccion, nombre=nombre_j)
                nombre_campo = f'pJ{numero_jornada}'
                setattr(objeto, nombre_campo, sec)
                objeto.save()

                objeto = get_object_or_404(Cartas_aux, nombre=nombre_j)
                #print(objeto)
                nombre_campo = f'j{numero_jornada}'
                setattr(objeto, nombre_campo, auxiliar)
                objeto.save()
            else:
                return render(request, 'llenar_quiniela/no_juego.html')
    else:
        nom = 'Seleccione'
        car = 'NC'
        equipos_disponibles_gol = []
        equipos_disponibles_tiempo = []
        equipos_disponibles_multi = []
        dicc_robo = []
    
    #print("SI")
    foto_url = []
    for registro in reg_im_car:
        #print(type(car), car)
        foto_url.append({
            'foto': getattr(registro, car),
        })
    #print("SI")
    #print(datos_procesados2)
    #print(foto_url)
    if car == 'DQ':
        consejo = 'DOBLE QUINIELA (DQ): Puedes llenar la quiniela como si fueran 2 (derecha e izquierda). Puedes repetir las predicciones que creas necesarias o puedes hacerlas completamente diferentes, tu eliges. La quiniela con mas puntos, es la que se queda.'
    elif car == 'IQ':
        consejo = 'ROBO DE PUNTOS (RP): Rellena tu quiniela de forma normal. Solo recuerda que al final de la jornada, puedes robarle los puntos a quien tu quieras (siempre y cuando no le hayan robado ya a esa persona) debes a visar a Choco a quien le quieres robar (tienes 3 dias para hacer el robo). Los puntos que tu haces, se los queda la otra persona'
    elif car == 'J':
        consejo = 'JUGADOR GOL (J): Rellena tu quiniela de forma normal. Selecciona el equipo donde están tus jugadores para echar gol (si el equipo no está disponible, entonces busca otros jugadores de otro equipo disponible). Por último, escribe el nombre de tus 2 jugadores.'
    elif car == 'M':
        consejo = 'MULTIPLICADOR (M): Rellena tu quiniela de manera normal y al final escoge al equipo que crees muy seguro que vas a atinar, ya que si lo atinas, tienes +2 puntos extra.'
    elif car == 'MA':
        consejo = 'MARCADOR (MA): Rellena la quiniela con los marcadores con los que crees que va a terminar el juego, si atinas el resultado, tienes +1 como normalmente sucede, pero si además atinas el marcador, tienes un +1 adicional.'
    elif car == 'NC':
        consejo = 'NO CARTA (NC): Si por alguna razón no tienes carta, llena tu quiniela de manera normal'
    elif car == 'OD':
        consejo = 'OPCION DOBLE (OD): Rellena tu quiniela como se muestra en la imagen. Tienes la posibilidad de seleccionar 3 juegos en los que puedes poner 2 opciones (Local y Empate, Local y Visita o Empate y Visita). Selecciona 3 juegos que tengas algo de dudas sobre quien va a ganar'
    elif car == 'OT':
        consejo = 'OPCION TRIPLE (OT): Rellena tu quiniela como se muestra en la imagen. Tienes la posibilidad de seleccionar 2 juegos en los que puedes poner las 3 opciones (Local, Empate y Visita). Selecciona 2 juegos que tengas algo de dudas sobre quien va a ganar y asegura esos resultados'
    elif car == 'RC':
        consejo = 'RULETA (RC): Gira una ruleta y deja que la suerte decida tu carta (dile a choco que te pase el link)'
    elif car == 'T':
        consejo = 'TIEMPO (T): Escribe un rango de tiempo (45 min, 30 min, 15 min o 5 min) en el que creas que un equipo (de tu elección) va a meter un gol. Dependiendo del rango que decidas, son los puntos extras que puedes acumular.'
    elif car == 'E':
        consejo = "ESTADISTICA (E): Escoge un equipo, luego, selecciona si crees que ese equipo quedará por arriba o por abajo de los momios. Cada acierto que hagas, tendrás +1 punto."
        #print("ESTA")
    #expl_cartas.append({
        
    #})
    #print(dicc_robo, car)
    
    nom_campo = f'j{numero_jornada}'
    #print(nom_campo)
    registros2 = Equipos.objects.all()
    registros_equipos = Equipos_fotos.objects.all()
    eq_quin = []
    fot_eq_quin = []
    
    for registro in registros2:
        secuencia = [item.strip() for item in getattr(registro, nom_campo).split(', ')]
    
    for r in registros_equipos:

        eq_j1 = secuencia[0].split(' vs ')
        eq1_j1 = eq_j1[0]
        pal = quitar_mayusculas_y_acentos(eq1_j1)
        foto_eq1_j1 = getattr(r, pal)
        eq2_j1 = eq_j1[1]
        pal = quitar_mayusculas_y_acentos(eq2_j1)
        foto_eq2_j1 = getattr(r, pal)
        
        eq_j2 = secuencia[1].split(' vs ')
        eq1_j2 = eq_j2[0]
        pal = quitar_mayusculas_y_acentos(eq1_j2)
        foto_eq1_j2 = getattr(r, pal)
        eq2_j2 = eq_j2[1]
        pal = quitar_mayusculas_y_acentos(eq2_j2)
        foto_eq2_j2 = getattr(r, pal)

        eq_j3 = secuencia[2].split(' vs ')
        eq1_j3 = eq_j3[0]
        pal = quitar_mayusculas_y_acentos(eq1_j3)
        foto_eq1_j3 = getattr(r, pal)
        eq2_j3 = eq_j3[1]
        pal = quitar_mayusculas_y_acentos(eq2_j3)
        foto_eq2_j3 = getattr(r, pal)
        
        eq_j4 = secuencia[3].split(' vs ')
        eq1_j4 = eq_j4[0]
        pal = quitar_mayusculas_y_acentos(eq1_j4)
        foto_eq1_j4 = getattr(r, pal)
        eq2_j4 = eq_j4[1]
        pal = quitar_mayusculas_y_acentos(eq2_j4)
        foto_eq2_j4 = getattr(r, pal)

        eq_j5 = secuencia[4].split(' vs ')
        eq1_j5 = eq_j5[0]
        pal = quitar_mayusculas_y_acentos(eq1_j5)
        foto_eq1_j5 = getattr(r, pal)
        eq2_j5 = eq_j5[1]
        pal = quitar_mayusculas_y_acentos(eq2_j5)
        foto_eq2_j5 = getattr(r, pal)
        
        eq_j6 = secuencia[5].split(' vs ')
        eq1_j6 = eq_j6[0]
        pal = quitar_mayusculas_y_acentos(eq1_j6)
        foto_eq1_j6 = getattr(r, pal)
        eq2_j6 = eq_j6[1]
        pal = quitar_mayusculas_y_acentos(eq2_j6)
        foto_eq2_j6 = getattr(r, pal)
        
        eq_j7 = secuencia[6].split(' vs ')
        eq1_j7 = eq_j7[0]
        pal = quitar_mayusculas_y_acentos(eq1_j7)
        foto_eq1_j7 = getattr(r, pal)
        eq2_j7 = eq_j7[1]
        pal = quitar_mayusculas_y_acentos(eq2_j7)
        foto_eq2_j7 = getattr(r, pal)
        
        eq_j8 = secuencia[7].split(' vs ')
        eq1_j8 = eq_j8[0]
        pal = quitar_mayusculas_y_acentos(eq1_j8)
        foto_eq1_j8 = getattr(r, pal)
        eq2_j8 = eq_j8[1]
        pal = quitar_mayusculas_y_acentos(eq2_j8)
        foto_eq2_j8 = getattr(r, pal)
        
        eq_j9 = secuencia[8].split(' vs ')
        eq1_j9 = eq_j9[0]
        pal = quitar_mayusculas_y_acentos(eq1_j9)
        foto_eq1_j9 = getattr(r, pal)
        eq2_j9 = eq_j9[1]
        pal = quitar_mayusculas_y_acentos(eq2_j9)
        foto_eq2_j9 = getattr(r, pal)
        
        eq_j10 = secuencia[9].split(' vs ')
        eq1_j10 = eq_j10[0]
        pal = quitar_mayusculas_y_acentos(eq1_j10)
        foto_eq1_j10 = getattr(r, 'inter')
        eq2_j10 = eq_j10[1]
        pal = quitar_mayusculas_y_acentos(eq2_j10)
        foto_eq2_j10 = getattr(r, 'inter')
        
        eq_j11 = secuencia[10].split(' vs ')
        eq1_j11 = eq_j11[0]
        pal = quitar_mayusculas_y_acentos(eq1_j11)
        foto_eq1_j11 = getattr(r, 'inter')
        eq2_j11 = eq_j11[1]
        pal = quitar_mayusculas_y_acentos(eq2_j11)
        foto_eq2_j11 = getattr(r, 'inter')
    
    eq_quin.append({
        'eq1_j1': eq1_j1,
        'eq2_j1': eq2_j1,
        'eq1_j2': eq1_j2,
        'eq2_j2': eq2_j2,
        'eq1_j3': eq1_j3,
        'eq2_j3': eq2_j3,
        'eq1_j4': eq1_j4,
        'eq2_j4': eq2_j4,
        'eq1_j5': eq1_j5,
        'eq2_j5': eq2_j5,
        'eq1_j6': eq1_j6,
        'eq2_j6': eq2_j6,
        'eq1_j7': eq1_j7,
        'eq2_j7': eq2_j7,
        'eq1_j8': eq1_j8,
        'eq2_j8': eq2_j8,
        'eq1_j9': eq1_j9,
        'eq2_j9': eq2_j9,
        'eq1_j10': eq1_j10,
        'eq2_j10': eq2_j10,
        'eq1_j11': eq1_j11,
        'eq2_j11': eq2_j11,
    })
    
    registros_equipos = Equipos_fotos.objects.all()
    diccio_fotos_equipos = []
    diccio_fotos_equipos.append({
        'eq1_j1': foto_eq1_j1,
        'eq2_j1': foto_eq2_j1,
        'eq1_j2': foto_eq1_j2,
        'eq2_j2': foto_eq2_j2,
        'eq1_j3': foto_eq1_j3,
        'eq2_j3': foto_eq2_j3,
        'eq1_j4': foto_eq1_j4,
        'eq2_j4': foto_eq2_j4,
        'eq1_j5': foto_eq1_j5,
        'eq2_j5': foto_eq2_j5,
        'eq1_j6': foto_eq1_j6,
        'eq2_j6': foto_eq2_j6,
        'eq1_j7': foto_eq1_j7,
        'eq2_j7': foto_eq2_j7,
        'eq1_j8': foto_eq1_j8,
        'eq2_j8': foto_eq2_j8,
        'eq1_j9': foto_eq1_j9,
        'eq2_j9': foto_eq2_j9,
        'eq1_j10': foto_eq1_j10,
        'eq2_j10': foto_eq2_j10,
        'eq1_j11': foto_eq1_j11,
        'eq2_j11': foto_eq2_j11,
    })
    dat_pro = jugadores_disponibles_robo(num_campo_robo_carta, numero_jornada)
    return render(request, 'llenar_quiniela/llenar_quiniela copy.html', {'imagenes': registros, 'cartas': dat_pro, 'carta_seleccionada': nom, 'foto_url': foto_url, 'consejo': consejo, 'jor': datos_procesados2, 'carta_quiniela': car, 'equipos_disponibles': equipos_disponibles_gol, 'diccio_robo': dicc_robo, 'diccio_equipos': eq_quin, 'fotos_equipos': diccio_fotos_equipos, 'Juegos_pendientes': jueg_pen, 'equipos_tiempo': equipos_disponibles_tiempo, 'equipos_multi': equipos_disponibles_multi, 'momios': momios})



