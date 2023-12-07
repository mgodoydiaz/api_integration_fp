# Se toma el archivo csv llamado metrica_numero.csv y se crea un archivo llamado metrica_numero.json

#import pandas

#Cargar como un dataframe el archivo csv
#df = pandas.read_csv('metrica_numero.csv')
#print(df)


dicc = {
    'Nombre':'Metrica Numero',
    'Autor': 'Miguel',
    'Datos':[]
    }

# Se rellenan los datos del diccionario con los datos del dataframe
# Columnas df
#columnas = ['Periodo', 'Trabajador', 'Fecha', 'Venta Diaria']

with open('metrica_numero.csv', 'r') as f:
    header = f.readline().strip().split(';')
    for linea in f:
        linea = linea.strip().split(';')
        dicc_linea = {}
        for i in range(len(linea)):
            dicc_linea[header[i]] = linea[i]
        dicc['Datos'].append(dicc_linea)           

# Se guarda el diccionario en un archivo json
import json
with open('JsonVarios\\metrica_numero.json', 'w') as f:
    json.dump(dicc, f, indent=4)
