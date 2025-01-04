import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutar la consulta SQL
cursor.execute('''
    SELECT nombre, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17 
    FROM tabla_general_jornadas
    ORDER BY suma_j DESC, suma_j_c DESC;
''')

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
#for resultado in resultados:
#    print(resultado)

# Cerrar la conexión
conexion.close()

#print("*"*20)
# Conectar a la base de datos SQLite
conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutar la consulta SQL
cursor.execute('''
    SELECT nombre, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17 
    FROM tabla_general_puntos_cartas;
''')

# Obtener los resultados de la consulta
resultados2 = cursor.fetchall()

# Imprimir los resultados
#for resultado in resultados2:
#    print(resultado)

# Cerrar la conexión
conexion.close()

# Lista de tuplas de puntajes

# Lista de diccionarios de puntajes
lista_diccionarios_puntajes = []
lista_diccionarios_cartas = []

# Función para convertir una tupla en un diccionario
def tupla_a_diccionario(tupla):
    return {
        'nombre': tupla[0],
        'j1': tupla[1],
        'j2': tupla[2],
        'j3': tupla[3],
        'j4': tupla[4],
        'j5': tupla[5],
        'j6': tupla[6],
        'j7': tupla[7],
        'j8': tupla[8],
        'j9': tupla[9],
        'j10': tupla[10],
        'j11': tupla[11],
        'j12': tupla[12],
        'j13': tupla[13],
        'j14': tupla[14],
        'j15': tupla[15],
        'j16': tupla[16],
        'j17': tupla[17],
    }

def cartas_a_diccionaario(tupla):
    return {
        'nombre': tupla[0],
        'j1': tupla[1],
        'j2': tupla[2],
        'j3': tupla[3],
        'j4': tupla[4],
        'j5': tupla[5],
        'j6': tupla[6],
        'j7': tupla[7],
        'j8': tupla[8],
        'j9': tupla[9],
        'j10': tupla[10],
        'j11': tupla[11],
        'j12': tupla[12],
        'j13': tupla[13],
        'j14': tupla[14],
        'j15': tupla[15],
        'j16': tupla[16],
        'j17': tupla[17],
    }

# Convertir cada tupla en un diccionario y agregarlo a la lista de diccionarios
for tupla_puntajes in resultados:
    diccionario_puntajes = tupla_a_diccionario(tupla_puntajes)
    lista_diccionarios_puntajes.append(diccionario_puntajes)

for tupla_puntajes in resultados2:
    diccionario_cartas = tupla_a_diccionario(tupla_puntajes)
    lista_diccionarios_cartas.append(diccionario_cartas)

# Imprimir la lista de diccionarios
#print(lista_diccionarios_puntajes)


valores = []
dc = ['Leo', 'Manuel', 'Luis Angel', 'Juan Luis', 'Omar', 'Hector', 'Horacio', 'Fernando', 'Bryan', 'Jorge', 'Josue', 'Rafa', 'Erick', 'Miguel', 'Alfonso', 'Saem']
posiciones_por_jornada = {nombre: [] for nombre in dc}
for jornada in range(1, 18):
    # Ordenar los registros en función del puntaje acumulado hasta la jornada actual
    lista_diccionarios_puntajes.sort(key=lambda x: sum(x[f'j{i+1}'] for i in range(jornada)), reverse=True)
    lista_diccionarios_cartas.sort(key=lambda x: sum(x[f'j{i+1}'] for i in range(jornada)), reverse=True)
    # Imprimir los resultados
    #print(f'Jornada {jornada}:')
    val = []
    val2 = []
    for i, registro in enumerate(lista_diccionarios_puntajes):
        lugar = i+1
        nombre = registro['nombre']
        puntos = sum(registro[f"j{i+1}"] for i in range(jornada))
        val.append({
            'nombre': nombre,
            'lugar': lugar,
            'puntos': puntos
        })
    for i, registro in enumerate(lista_diccionarios_cartas):
        lugar = i+1
        nombre = registro['nombre']
        puntos = sum(registro[f"j{i+1}"] for i in range(jornada))
        val2.append({
            'nombre': nombre,
            'lugar': lugar,
            'puntos': puntos
        })
    # Combinar los diccionarios
    diccionario_combinado = {}
    for d in val:
        diccionario_combinado[d['nombre']] = {'puntos1': d['puntos']}
    for d in val2:
        diccionario_combinado[d['nombre']]['puntos2'] = d['puntos']

    # Ordenar el diccionario combinado
    diccionario_ordenado = sorted(diccionario_combinado.items(), key=lambda x: (x[1]['puntos1'], x[1]['puntos2']), reverse=True)

    # Imprimir el diccionario ordenado
    for i, (nombre, puntos) in enumerate(diccionario_ordenado):
        posiciones_por_jornada[nombre].append(i + 1)

#for nombre, posiciones in posiciones_por_jornada.items():
#    print(f'{nombre}: {posiciones}')
#print("*"*30)


# Crear una figura y ejes para el gráfico
fig, ax = plt.subplots()

lineas = []
etiquetas = []
# Iterar sobre cada jugador
for nombre, posiciones in posiciones_por_jornada.items():
    # Dibujar las posiciones del jugador en cada jornada
    linea, = ax.plot(range(1, 18), posiciones, label=nombre)
    lineas.append(linea)
    etiquetas.append(nombre)


# Configurar el gráfico
ax.set_xlabel('Jornada')
ax.set_ylabel('Posición')
ax.set_title('Posiciones de los jugadores a lo largo de las 17 jornadas')
ax.legend()

# Invertir el eje y
ax.invert_yaxis()

# Cambiar la escala del eje y para que se vean de 1 en 1
ax.set_yticks(range(1, 18))
ax.set_yticklabels(range(1, 18))
ax.set_xticks(range(1, 18))
ax.set_xticklabels(range(1, 18))

# Función para resaltar una gráfica seleccionada y atenuar las demás
def resaltar_grafica(evento):
    for i, linea in enumerate(lineas):
        # Obtener las coordenadas de los datos de la línea
        x, y = linea.get_data()
        # Verificar si el evento está dentro del área de datos de la línea
        if linea.contains(evento)[0]:
            linea.set_alpha(1.0)  # Resaltar la gráfica seleccionada
            ax.legend([linea], [etiquetas[i]], loc='upper left')  # Actualizar la leyenda
        else:
            linea.set_alpha(0.3)  # Atenuar las demás gráficas
    fig.canvas.draw_idle()

# Conectar la función resaltar_grafica al evento motion_notify
fig.canvas.mpl_connect('motion_notify_event', resaltar_grafica)

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutar la consulta SQL
cursor.execute('''
    SELECT nombre, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17 
    FROM tabla_general_cartas;
''')

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Crear un diccionario para almacenar las opciones de cada jugador
opciones_por_jugador = {}

# Iterar sobre cada resultado
for resultado in resultados:
    # Obtener el nombre del jugador
    nombre = resultado[0]
    # Contar las opciones de cada jugador
    opciones = {'NC': 0, 'OD': 0, 'J': 0, 'DQ': 0, 'OT': 0, 'MA': 0, 'M': 0, 'IQ': 0}
    for opcion in resultado[1:]:
        opciones[opcion] += 1
    # Almacenar las opciones de cada jugador en el diccionario
    opciones_por_jugador[nombre] = opciones

# Iterar sobre cada jugador
for jugador, opciones in opciones_por_jugador.items():
    # Crear una figura y ejes para el gráfico de pastel
    fig, ax = plt.subplots()
    # Crear un gráfico de pastel para cada jugador
    ax.pie(opciones.values(), labels=opciones.keys(), autopct='%1.1f%%')
    ax.set_title(f'Opciones de {jugador}')
    # Mostrar el gráfico de pastel
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

