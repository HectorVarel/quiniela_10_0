import sqlite3
import os
import django

nj = 3
nj_p = 2
Manuel_p = 'V, V, LE, E, LV, V, L, L, V, V, V'
Manuel_c = 'DQ'
Manuel_c_aux = 'NA'
Manuel_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Leo_p = 'V, V, L, LE, L, V, L, L, V, V, LV'
Leo_c = 'NC'
Leo_c_aux = 'NA'
Leo_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Luis_Angel_p = 'V, V, L, L, L, V, L, L, E, V, L'
Luis_Angel_c = 'MA'
Luis_Angel_c_aux = 'NA'
Luis_Angel_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Horacio_p = 'EV, EE, LL, LE, LE, VV, LE, LL, VV, LE, LL'
Horacio_c = 'NC'
Horacio_c_aux = 'NA'
Horacio_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Juan_Luis_p = 'V, V, L, L, L, V, LEV, E, V, V, L'
Juan_Luis_c = 'MA'
Juan_Luis_c_aux = 'NA'
Juan_Luis_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Jorge_p = 'V, LV, L, L, E, L, LV, E, V, L, L'
Jorge_c = 'NC'
Jorge_c_aux = 'NA'
Jorge_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Rafa_p = 'V, V, L, L, L, V, E, E, V, V, V'
Rafa_c = 'MA'
Rafa_c_aux = 'NA'
Rafa_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Fernando_p = 'V, L, E, V, L, V, L, E, V, E, L'
Fernando_c = 'NC'
Fernando_c_aux = 'NA'
Fernando_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Bryan_p = 'EL, VE, LL, EL, LL, VE, LE, EE, VE, VE, LE'
Bryan_c = 'NC'
Bryan_c_aux = 'NA'
Bryan_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Saem_p = 'VV, EE, LL, LE, LL, VV, EE, LV, VE, EV, VV'
Saem_c = 'DQ'
Saem_c_aux = 'NA'
Saem_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Miguel_p = 'V, V, L, L, E, V, L, E, V, V, V'
Miguel_c = 'NC'
Miguel_c_aux = 'NA'
Miguel_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Alfonso_p = 'V, V, E, L, L, V, E, E, V, L, V'
Alfonso_c = 'NC'
Alfonso_c_aux = 'NA'
Alfonso_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Hector_p = 'E, V, LE, L, L, V, L, E, V, E, EV'
Hector_c = 'M'
Hector_c_aux = '4'
Hector_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Josue_p = 'V, E, L, L, L, V, E, L, V, V, V'
Josue_c = 'NC'
Josue_c_aux = 'NA'
Josue_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Erick_p = 'LEV, V, L, LEV, L, V, V, L, V, V, V'
Erick_c = 'NC'
Erick_c_aux = 'NA'
Erick_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Omar_p = 'V, V, L, E, L, V, L, L, V, E, V'
Omar_c = 'M'
Omar_c_aux = '4'
Omar_p_p = 'X, X, X, X, X, X, X, X, X, X, X'

Resultados = '1-1, 1-1, 2-1, 3-2, 3-1, 0-0, 3-1, 2-1, 1-1, 5-2, 0-0'
Resultados_p = 'NA, NA, NA, NA, NA, NA, NA, NA, 3-2, NA, NA'
Resultados_c = 'NO'
Resultados_c_aux = 'NA'
jug_gol = ['Toro']

Jugadores = ['Manuel', 'Leo','Luis Angel', 'Horacio', 'Juan Luis', 'Jorge', 'Rafa', 'Fernando', 'Bryan', 'Saem', 'Miguel', 'Alfonso', 'Hector', 'Josue', 'Erick', 'Omar', 'Resultados']
Jugadores_p = [Manuel_p, Leo_p, Luis_Angel_p, Horacio_p, Juan_Luis_p, Jorge_p, Rafa_p, Fernando_p, Bryan_p, Saem_p, Miguel_p, Alfonso_p, Hector_p, Josue_p, Erick_p, Omar_p, Resultados]
Jugadores_c = [Manuel_c, Leo_c, Luis_Angel_c, Horacio_c, Juan_Luis_c, Jorge_c, Rafa_c, Fernando_c, Bryan_c, Saem_c, Miguel_c, Alfonso_c, Hector_c, Josue_c, Erick_c, Omar_c, Resultados_c]
Jugadores_c_aux = [Manuel_c_aux, Leo_c_aux, Luis_Angel_c_aux, Horacio_c_aux, Juan_Luis_c_aux, Jorge_c_aux, Rafa_c_aux, Fernando_c_aux, Bryan_c_aux, Saem_c_aux, Miguel_c_aux, Alfonso_c_aux, Hector_c_aux, Josue_c_aux, Erick_c_aux, Omar_c_aux, Resultados_c_aux]
Jugadores_p_p = [Manuel_p_p, Leo_p_p, Luis_Angel_p_p, Horacio_p_p, Juan_Luis_p_p, Jorge_p_p, Rafa_p_p, Fernando_p_p, Bryan_p_p, Saem_p_p, Miguel_p_p, Alfonso_p_p, Hector_p_p, Josue_p_p, Erick_p_p, Omar_p_p, Resultados_p]

def acceder_predicciones(nom, nj):
    jornada = f'pj{nj}'
    # Conectar a la base de datos SQLite3
    conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
    cursor.execute("SELECT nombre, " + jornada + " FROM llenar_quiniela_Prediccion WHERE nombre = '"+ nom +"'")

    # Obtener todos los resultados
    resultados = cursor.fetchall()

    # Mostrar resultados
    #for resultado in resultados:
    #    print(resultado)

    # Cerrar la conexión
    conexion.close()

def actualizar_predicciones(nom, nj, p):
    jornada = f'pJ{nj}'
    # Conectar a la base de datos SQLite3
    conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
    
    sql_query = "UPDATE llenar_quiniela_Prediccion SET " + jornada + " = '" + p + "' WHERE nombre = '"+ nom +"';"
    
    cursor.execute(sql_query)
    resultados = cursor.fetchall()

    #for resultado in resultados:
    #    print('Posible actualizacion', resultado)

    conexion.commit()

    # Cerrar la conexión
    conexion.close()

def marcador_a_secuencia(secuencia):
    elementos = secuencia.split(', ')

    letras_resultado = []

    for elemento in elementos:
        if '-' in elemento:
            numero1, numero2 = map(int, elemento.split('-'))

            if numero1 > numero2:
                letras_resultado.append('L')
            elif numero1 < numero2:
                letras_resultado.append('V')
            else:
                letras_resultado.append('E')
        else:
            letras_resultado.append(elemento)

    return ', '.join(letras_resultado)

def extra_points(carta, carta_aux, jug_gol, correctos, pred, pred_n, pred_j_n, colo):
    puntos = 0
    if carta == 'J':
        if carta_aux in jug_gol:
            puntos = 2
        #print('Puntos por jugador que mete gol: ', puntos)
    elif carta == 'M':
        if correctos[int(carta_aux)] == pred[int(carta_aux)]:
            puntos = 2
            colo[int(carta_aux)] = 'goldenrod'
        #print('Puntos por el Multiplicador: ', puntos)
    elif carta == 'MA':
        s1 = [item.strip() for item in pred_n.split(',')]
        s2 = [item.strip() for item in pred_j_n.split(',')]
        c = []
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                puntos += 1
                c.append(i)
        for i in c:
            colo[i] = 'aquamarine'
        #print('Puntos por el Marcador: ', puntos)
    else:
        #print('No hay puntos extra')
        puntos = 0
    return puntos, colo

def actualizar_quiniela_pendiente(sec_pen, nj, nombre):
    jornada = f'pj{nj}'
    # Conectar a la base de datos SQLite3
    conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
    
    sql_query = "SELECT " + jornada + " FROM llenar_quiniela_Prediccion WHERE nombre = '"+ nombre +"'"
    
    cursor.execute(sql_query)
    resultados = cursor.fetchall()
    res = resultados[0][0].split(', ')
    sec = [item.strip() for item in sec_pen.split(',')]
    new_seq = []
    if nombre == 'Resultados':
        for r in range(len(res)):
            if res[r] == 'NA':
                new_seq.append(sec[r])
            else:
                new_seq.append(res[r])
    else:
        for r in range(len(res)):
            if res[r] == 'X':
                new_seq.append(sec[r])
            else:
                new_seq.append(res[r])
    #print(new_seq)
    sec_res = ', '.join(new_seq)
    conexion.commit()

    # Cerrar la conexión
    conexion.close()

    conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
    
    sql_query = "UPDATE llenar_quiniela_prediccion SET " + jornada + " = '"+ sec_res +"' WHERE nombre = '"+ nombre +"'"
    cursor.execute(sql_query)
    conexion.commit()

    # Cerrar la conexión
    conexion.close()

    return sec_res

def get_points(prediccion_n, prediccion_s, carta, pred_j, carta_aux, jug_gol):
    sec_colores = ['lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon', 'lightsalmon']
    correctos = [item.strip() for item in prediccion_s.split(',')]
    pred = [item.strip() for item in pred_j.split(',')]
    p_extra = 0
    #print(prediccion_s)
    #print(pred_j)
    # Suma de puntos para Opcion doble y Opcion triple
    if carta == 'OD' or carta == 'OT' or carta == 'IQ' or carta == 'NC':
        contador = 0
        for idx, (valor1, valor2) in enumerate(zip(correctos, pred)):
            if len(valor2) == 1:
                if valor1 == valor2 or valor1 in valor2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'

            else:
                subvalores2 = [valor2[i:i+1] for i in range(0, len(valor2), 1)]
                if valor1 == valor2 or valor1 in subvalores2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'
        #print(contador)
    elif carta == 'DQ':
        q1 = [elemento[0] for elemento in pred]
        q2 = [elemento[1] for elemento in pred]
        arr_col1 = []
        arr_col2 = []
        contador_q1 = 0
        for idx, (valor1, valor2) in enumerate(zip(correctos, q1)):
            if len(valor2) == 1:
                if valor1 == valor2 or valor1 in valor2:
                    contador_q1 += 1
                    arr_col1.append(idx)
            else:
                subvalores2 = [valor2[i:i+1] for i in range(0, len(valor2), 1)]
                if valor1 == valor2 or valor1 in subvalores2:
                    contador_q1 += 1
                    arr_col1.append(idx)
        contador_q2 = 0
        for idx, (valor1, valor2) in enumerate(zip(correctos, q2)):
            if len(valor2) == 1:
                if valor1 == valor2 or valor1 in valor2:
                    contador_q2 += 1
                    arr_col2.append(idx)
            else:
                subvalores2 = [valor2[i:i+1] for i in range(0, len(valor2), 1)]
                if valor1 == valor2 or valor1 in subvalores2:
                    contador_q2 += 1
                    arr_col2.append(idx)
        if contador_q1 > contador_q2:
            contador = contador_q1
            for i in arr_col1:
                sec_colores[i] = 'lightgreen'
            q = q1
        elif contador_q2 > contador_q1:
            contador = contador_q2
            for i in arr_col2:
                sec_colores[i] = 'lightgreen'
            q = q2
        else:
            contador = contador_q1
            for i in arr_col1:
                sec_colores[i] = 'lightgreen'
            q = q1

        #print('Doble Quiniela: ', contador, q)
    elif carta == 'J':
        contador = 0
        for idx, (valor1, valor2) in enumerate(zip(correctos, pred)):
            if len(valor2) == 1:
                if valor1 == valor2 or valor1 in valor2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'
            else:
                subvalores2 = [valor2[i:i+1] for i in range(0, len(valor2), 1)]
                if valor1 == valor2 or valor1 in subvalores2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'
        p_extra, sec_colores = extra_points(carta, carta_aux, jug_gol, correctos, pred, prediccion_n, pred_j, sec_colores)
        contador += p_extra
        #print('Jugador: ', contador)
    elif carta == 'M':
        pred_M = [letra.upper() for letra in pred]
        contador = 0
        for idx, (valor1, valor2) in enumerate(zip(correctos, pred_M)):
            if len(valor2) == 1:
                if valor1 == valor2 or valor1 in valor2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'
            else:
                subvalores2 = [valor2[i:i+1] for i in range(0, len(valor2), 1)]
                if valor1 == valor2 or valor1 in subvalores2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'
        p_extra, sec_colores = extra_points(carta, carta_aux, jug_gol, correctos, pred, prediccion_n, pred_j, sec_colores)
        contador += p_extra
        #print('Multiplicador: ', contador)
    elif carta == 'MA':
        q_s = marcador_a_secuencia(pred_j)
        q_s = [item.strip() for item in q_s.split(',')]
        contador = 0
        for idx, (valor1, valor2) in enumerate(zip(correctos, q_s)):
            if len(valor2) == 1:
                if valor1 == valor2 or valor1 in valor2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'
            else:
                subvalores2 = [valor2[i:i+1] for i in range(0, len(valor2), 1)]
                if valor1 == valor2 or valor1 in subvalores2:
                    contador += 1
                    sec_colores[idx] = 'lightgreen'
        p_extra, sec_colores = extra_points(carta, carta_aux, jug_gol, correctos, pred, prediccion_n, pred_j, sec_colores)
        contador += p_extra
        #print('Marcador: ', contador)
    else:
        contador = 0
        #print('No aplica')
    #print(correctos, pred)
    cadena_resultante = ', '.join(sec_colores)
    return contador, p_extra, cadena_resultante

def actualizar_puntos(nombre, nj, puntos, puntos_extra):

    if nombre != 'Resultados':
        #print(puntos_extra)
        jornada = f'J{nj}'
        # Conectar a la base de datos SQLite3
        conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
        
        sql_query = "UPDATE tabla_general_jornadas SET " + jornada + " = '" + str(puntos) + "' WHERE nombre = '"+ nombre +"';"
        
        cursor.execute(sql_query)

        #for resultado in resultados:
        #    print('Posible actualizacion', resultado)

        conexion.commit()

        # Cerrar la conexión
        conexion.close()

        jornada = f'j{nj}'

        # Conectar a la base de datos SQLite3
        conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
        
        sql_query = "UPDATE tabla_general_puntos_extra SET " + jornada + " = '" + str(puntos_extra) + "' WHERE nombre = '"+ nombre +"';"
        
        cursor.execute(sql_query)

        #for resultado in resultados:
        #    print('Posible actualizacion', resultado)

        conexion.commit()

        # Cerrar la conexión
        conexion.close()

def actualizar_suma_puntos(nombre):
    if nombre != 'Resultados':
        # Conectar a la base de datos SQLite3
        conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
        
        sql_query = "SELECT j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17 FROM tabla_general_jornadas WHERE nombre =  '"+ nombre +"'"
        
        cursor.execute(sql_query)
        resultados = cursor.fetchall()
        #suma = sum(resultados)

        for res in resultados:
            suma = sum(res)
        
        # Consulta SQL con placeholders
        sql_query = "UPDATE tabla_general_jornadas SET suma_j = ? WHERE nombre = ?"

        # Ejecutar la consulta con la tupla de parámetros
        cursor.execute(sql_query, (suma, nombre))
        #for resultado in resultados:
        #    print('Posible actualizacion', resultado)

        conexion.commit()

        # Cerrar la conexión
        conexion.close()

def actualizar_cartas(nombre, carta, nj):
    jornada = f'j{nj}'
    if nombre != 'Resultados':
        # Conectar a la base de datos SQLite3
        conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
        
        sql_query = "UPDATE tabla_general_Cartas SET '"+ jornada +"' = '"+ carta +"' WHERE nombre =  '"+ nombre +"'"
        
        cursor.execute(sql_query)
        
        conexion.commit()

        # Cerrar la conexión
        conexion.close()


def actualizar_colores(nombre, sec_colores, nj):
    jornada = f'j{nj}'
    if nombre != 'Resultados':
        # Conectar a la base de datos SQLite3
        conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
        
        sql_query = "UPDATE tabla_general_Colores SET '"+ jornada +"' = '"+ sec_colores +"' WHERE nombre =  '"+ nombre +"'"
        
        cursor.execute(sql_query)
        
        conexion.commit()

        # Cerrar la conexión
        conexion.close()

###################
def sec_resultados(nj):
    jornada = f'pj{nj}'
    # Conectar a la base de datos SQLite3
    conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
    cursor.execute("SELECT " + jornada + " FROM llenar_quiniela_Prediccion WHERE nombre = Resultados")

    # Obtener todos los resultados
    resultados = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    return resultados
###################

"""
Resultados_s = marcador_a_secuencia(Resultados)
for n in range(len(Jugadores)):
    actualizar_predicciones(Jugadores[n], nj, Jugadores_p[n])
    puntos, puntos_extra, sec_colores = get_points(Resultados, Resultados_s, Jugadores_c[n], Jugadores_p[n], Jugadores_c_aux[n], jug_gol)
    #print('El jugador: ', Jugadores[n], ' tiene: ', puntos, ' puntos')
    actualizar_puntos(Jugadores[n], nj, puntos, puntos_extra)
    actualizar_suma_puntos(Jugadores[n])
    actualizar_cartas(Jugadores[n], Jugadores_c[n], nj)
    actualizar_colores(Jugadores[n], sec_colores, nj)
    #acceder_predicciones(Jugadores[n], nj)

"""
jornada = f'pj{nj_p}'
# Conectar a la base de datos SQLite3
conexion = sqlite3.connect('C:/Users/varel/Documents/ProjectDjango/quiniela/db.sqlite3')

# Crear un cursor
cursor = conexion.cursor()

# Ejecutar una consulta (por ejemplo, seleccionar todos los registros)
    
sql_query = "SELECT " + jornada + " FROM llenar_quiniela_Prediccion WHERE nombre = 'Resultados'"
  
cursor.execute(sql_query)
resultados = cursor.fetchall()
res = resultados[0][0].split(', ')
sec = [item.strip() for item in Resultados_p.split(',')]
new_seq = []

for r in range(len(res)):
    if res[r] == 'NA':
        new_seq.append(sec[r])
    else:
        new_seq.append(res[r])
#print(new_seq)
sec_res = ', '.join(new_seq)
conexion.commit()
#print(Resultados)
#print(sec_res)
# Cerrar la conexión
conexion.close()
Resultados_s_p = marcador_a_secuencia(sec_res)
#print(Resultados_s)
#print(Resultados_s_p)
Jugadores_p_pp = []
for n in range(len(Jugadores)):
    sec_actualizada = actualizar_quiniela_pendiente(Jugadores_p_p[n], nj_p, Jugadores[n])
    acceder_predicciones(Jugadores[n], nj_p)
    print("Jugador: ", Jugadores[n])
    print("Secuencia de res: ", sec_actualizada)
    print("Resultados_s_p: ", Resultados_s_p)
    print("*"*20)
    #print(Juan_Luis_p_p[n])
    #print(Resultados_s_p)
    #print("***************")
    puntos, puntos_extra, sec_colores = get_points(sec_res, Resultados_s_p, Jugadores_c[n], sec_actualizada, Jugadores_c_aux[n], jug_gol)
    actualizar_puntos(Jugadores[n], nj_p, puntos, puntos_extra)
    actualizar_suma_puntos(Jugadores[n])
    actualizar_colores(Jugadores[n], sec_colores, nj_p)

