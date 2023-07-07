# -*- coding: utf-8 -*-
"""
Módulo de funciones de organización de bases de datos

Created on Mon Jun 26 20:51:55 2023

@author: rafle
"""
import pandas as pd

def agruparColumnas (database, pregunta, sufijo_pregunta, id_elemento, max_elementos):
    # revisa la pregunta  para todos los actores (n)
    columns = []
    for i in range(1,max_elementos+1):
        col = pregunta+str(i)+sufijo_pregunta
        columns.append(col)
    #print(columns)
    mergedColExample = pd.melt(database, id_vars=['Result Id'], 
                               value_vars=columns, 
                               var_name = pregunta+"-"+sufijo_pregunta, 
                               value_name = (pregunta+sufijo_pregunta))
    mergedColExample[id_elemento] = mergedColExample[pregunta+"-"+sufijo_pregunta].str.extract(r'\((\d+)\)')
    mergedColExample = mergedColExample.sort_values(['Result Id',id_elemento], 
                                                    ascending = [True,True])
    return mergedColExample

def separar_entidades_nivel1(database, vector_tipologia, vector_preguntas, nombre_bd, id_elemento, max_amount_elementos):
    i = 0
    for tipo in vector_tipologia:
        variable_compilada = agruparColumnas(database, tipo[0], tipo[1], id_elemento, max_amount_elementos)
        if i > 0:
            base_compilacion = base_compilacion.merge(variable_compilada, on = ['Result Id',vector_preguntas[1]])
        else:
            base_compilacion = variable_compilada
            pregunta_inicial = tipo[0]+tipo[1]
        i = i + 1
        vector_preguntas.append(tipo[0]+tipo[1])
    base_compilacion = base_compilacion[vector_preguntas]
    base_compilacion = base_compilacion[base_compilacion[pregunta_inicial]!=""]
    base_compilacion.to_csv(nombre_bd+'.csv', encoding="utf-8-sig")
    return base_compilacion

def fusionar_preguntas(data_frame):
    ## Esta función revisa cada pregunta y agrupa sus opciones en la primera columna
    i = 0
    fin = 0 
    for column in data_frame:
        # Revisar columna por columna, contar espacios cuando se encuentren 
        # columnas vacías
        if column[0:7] == "Unnamed":
            if fin == 0:
                inicio = i-1
            #print("columna repetida {} veces".format(fin))
            fin = fin +1
        else:
            # Si la columna tiene nombre, agrupar anterior compilación y seguir
            if fin > 0:
                #print("Ejecutando Join con inicio {0} y fin {1}".format(inicio ,(inicio+fin+1)))
                columna = data_frame.columns[inicio]
                #print(columna)
                data_frame[columna] = data_frame[data_frame.columns[inicio:(inicio+fin+1)]].apply(lambda x:'.'.join(x.dropna().astype(str)),axis = 1)
                fin = 0
            else:
                fin = 0
                preg_actual = column
        i = i +1
    return data_frame

                
                
                                                                                
                
                                                                                
#separar_entidades_nivel1(data, vehiculos, ['Result Id','id_veh'], "03_vehiculos", 'id_veh', Max_veh)