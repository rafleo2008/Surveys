# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 19:42:17 2023

@author: rafle
"""

from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
#import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd
import datetime
import io
import base64

import funciones as f
import parametros as p

app = Dash(__name__)

app = Dash(prevent_initial_callbacks=True)
app.title = "Procesamiento base CTG"
app.description = "Descripción de prueba"

server = app.server

## Layout

## Callbacks

## results

app.layout = html.Div(
    [
     html.H1(children = "Herramienta para reorganizar base de datos CTG", style = {'textAlign':'center'}),
     html.H2(children = "1. Por favor Cargue el archivo de base plana (formato excel)"),
     html.H3(children = "El aplicativo solo recibe archivos .csv, por favor guarde como la base antes de subirla"),
     html.Div([
         dcc.Upload(
             id = "upload-data",
             children = html.Div([
                 "Arrastre el archivo .csv o ",
                 html.A("Seleccione los archivos")
             ]),
             style = {
                 'width': '60%',
                 'height': '60px',
                 'lineHeight': '60px',
                 'bordeWidth':'1px',
                 'borderStyle':'dashed',
                 'borderRadius':'5px',
                 'textAlign':'center',
                 'margin':'10px'
             },
             multiple = True  
         ),
     dcc.Store(id = 'intermediate_bd'),
     dcc.Store(id = 'base_procesada'),
     dcc.Store(id = "hogares"),
     dcc.Store(id = "personas"),
     dcc.Store(id = "vehiculos"),
     dcc.Store(id = "viajes"),
     html.Div(id = 'output-uploader-example'),
     html.Div(id = 'button_zone')])
     #html.Button("Descargar hogares csv", id= 'hogares_btn'),
     #dcc.Download(id = 'download_hogares')])
     ])
### Funciones auxiliares del front-end

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    #print(decoded)
    try:
        #if 'csv' in filename:
        if filename.endswith('.csv'):
            data = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            data = pd.read_excel(io.BytesIO(decoded))
        ## Aquí va la función de organización

    except Exception as e:
        print(e)
        #return html.Div(['El archivo no es de un formato válido, pruebe con .csv o .xlsx, nombre '+filename],
    return data.to_json(date_format='iso', orient='split')

### Sección de Callbacks

## Callback para el cargador de archivo
@callback(
    Output(component_id = "intermediate_bd", component_property = "data"),
    Output(component_id = "button_zone", component_property = "children"),
    Input("upload-data", "contents"),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified')
    )
def run_and_update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        database = [
            parse_contents (c, n, d) for c, n, d in 
            zip(list_of_contents, list_of_names, list_of_dates)
        ]
        children = ([
            html.Button("Descargar hogares csv", id= 'hogares_btn'),
            dcc.Download(id = 'download_hogares'),
            html.Button("Descargar personas csv", id ='personas_btn'),
            dcc.Download(id = 'download_personas'),
            html.Button("Descargar vehiculos csv", id ='veh_btn'),
            dcc.Download(id = 'download_veh'),
            html.Button("Descargar viajes  csv", id ='viajes_btn'),
            dcc.Download(id = 'download_viajes')
        ])
    
        return database, children

## Callback para primer procesamiento de base de datos

@callback(
    Output('base_procesada', 'data'),
    Input('intermediate_bd', 'data'))
    # Se recibe la base de datos y se ajusta para cargar las opciones en 1 columna
def preparar_base(data):
    print('Iniciando preparación preliminar')
    data = pd.read_json(data[0], orient='split')
    i = 0 
    fin = 0 
    for column in data:
        #print(column)
        if column[0:7] == "Unnamed":
            if fin == 0:
                inicio = i-1   
            #print("columna repetida {} veces".format(fin))
            fin = fin + 1
        else:
            # Si hubo unnamed previos, correr funcion
            if fin > 0:
                #print("Ejecutando Join con inicio {0} y fin {1}".format(inicio ,(inicio+fin+1)))
                columna = data.columns[inicio]
                #print(columna)
            
                data[columna] = data[data.columns[inicio:(inicio+fin+1)]].apply(lambda x:'.'.join(x.dropna().astype(str)),
                                                                         axis = 1)
                fin = 0
            else:          
                fin = 0
                preg_actual = column
        i = i+1
    print("Preprocesamiento ejecutado sin problemas")
    return data.to_json(date_format='iso', orient='split')
        
## Callback para crear hogares

@callback(
    Output('hogares', 'data'),
    #Input(),
    Input(component_id = 'base_procesada', component_property = 'data'))
def organizar_hogares (data):
    # se recibe la base de datos agrupada y se separan las columnas de hogares

    print("Estamos leyendo la base de datos intermedia")
    data = pd.read_json(data, orient='split')
    hogares = data.loc[:, p.hogares]
    hogares = hogares.drop(0, axis =0)
    print("Hogares creados")
    return hogares.to_json(date_format='iso', orient='split')

## Callback para crear personas, vehículos y viajes
@callback(
    Output('personas', 'data'),
    Output('vehiculos', 'data'),
    Output('viajes','data'),
    Input(component_id = 'base_procesada', component_property = 'data'))
def crear_encuesta (data):
    print("Inicia el módulo de creación de personas, vehiculos y viajes")
    data = pd.read_json(data, orient='split')
    personas_bd = f.separar_entidades_nivel1(data, p.personas, ['Result Id','id_per'], "02_personas", 'id_per', p.Max_per)
    vehiculos_bd = f.separar_entidades_nivel1(data, p.vehiculos, ['Result Id','id_veh'], "03_vehiculos", 'id_veh', p.Max_veh)
    viajes_bd = f.separar_entidades_nivel1(data, p.viajes, ['Result Id','id_viaje'], "04_viajes", 'id_viaje', p.Max_per)
    ## Ajustes adicionales de viajes

    viajes_bd = viajes_bd.rename(columns = {'Q37.() Número de residente': 'id_per'})
    viajes_bd = viajes_bd.drop(['id_viaje'], axis = 1)
    viajes_bd = viajes_bd[viajes_bd['id_per'].notna()]
    viajes_bd = viajes_bd.sort_values(by=['Result Id', 'id_per','Q38.() Número de viaje'],
                                    ascending = [True,True, True])
    print(viajes_bd)

    
    print("Bases de personas, vehiculos y viajes creadas correctamente")
    personas_bd = personas_bd.to_json(date_format = 'iso', orient = 'split')
    vehiculos_bd = vehiculos_bd.to_json(date_format = 'iso', orient = 'split')
    viajes_bd = viajes_bd.to_json(date_format = 'iso', orient = 'split')
    return personas_bd, vehiculos_bd, viajes_bd

### Callback para descargar base de hogares
@callback(
    Output("download_hogares", "data"),
    Input("hogares_btn","n_clicks" ),
    Input("hogares", "data"))
def download_hogares (n_clicks, data):
    
    data = pd.read_json(data, orient='split')
    return dcc.send_data_frame(data.to_csv, filename = "hogares.csv", encoding="utf-8-sig")
### Callback para descargar base de personas
@callback(
    Output("download_personas", "data"),
    Input("personas_btn", "n_clicks"),
    Input("personas", "data"))
def download_personas(n_clicks, data):
    
    data = pd.read_json(data, orient='split')
    return dcc.send_data_frame(data.to_csv, filename = "personas.csv", encoding="utf-8-sig")
### Callback para descargar base de vehiculos
@callback(
    Output("download_veh", "data"),
    Input("veh_btn", "n_clicks"),
    Input("vehiculos", "data"))
def download_vehiculos(n_clicks, data):
    
    data = pd.read_json(data, orient='split')
    return dcc.send_data_frame(data.to_csv, filename = "vehiculos.csv", encoding="utf-8-sig")
### Callback para descargar base de viajes
@callback(
    Output("download_viajes", "data"),
    Input("veh_btn", "n_clicks"),
    Input("viajes", "data"))
def download_viajes(n_clicks, data):
    
    data = pd.read_json(data, orient='split')
    return dcc.send_data_frame(data.to_csv, filename = "viajes.csv", encoding="utf-8-sig")


    


### Iniciar servidor



if __name__ == '__main__':
    app.run(debug=True, port=3030)

    
