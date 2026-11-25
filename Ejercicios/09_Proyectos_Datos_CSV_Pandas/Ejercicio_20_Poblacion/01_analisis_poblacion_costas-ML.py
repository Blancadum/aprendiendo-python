"""
Ejercicio 20: Análisis estadístico y demográfico de municipios (poblacion.csv)

Enunciado:
A partir del archivo 'poblacion.csv' (que contiene datos censales, kilómetros de costa,
playas, viviendas y habitantes de diferentes municipios):
1. Calcular el número de municipios de la provincia con mar.
2. Calcular el número de municipios con más de 15.000 habitantes.
3. Calcular la suma total de playas de la provincia.
4. Calcular la suma total de habitantes que viven en municipios costeros.
5. Calcular la suma total de habitantes que viven en municipios de menos de 5.000 habitantes.
6. Calcular la suma total de kilómetros de costa de la provincia.
7. Calcular la suma total de viviendas en municipios costeros.
8. Calcular la densidad de población en municipios costeros (viviendas costa / habitantes costa).
9. Calcular la densidad de población en municipios no costeros (viviendas no costa / habitantes no costa).
10. Generar los archivos 'resultado.csv' y 'soluciones.csv' para verificar la concordancia exacta de los datos calculados.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
import subprocess

# Limpiar consola de forma multiplataforma
os.system("cls" if os.name == "nt" else "clear")

# Obtener la ruta del directorio del script actual
ruta = os.path.dirname(os.path.abspath(__file__))

datos_leidos = list() 

# Sin el encoding, no se puede leer el csv
with open(ruta + "/poblacion.csv", mode="r", encoding="latin-1") as datos:
    contenido = datos.readlines()
    for i in range(len(contenido)):
        if(i > 0):
            registro = contenido[i].replace('\n', '')
            datos_leidos.append(registro.split(";"))

def calcular_municipios_mar(datos: list[str]):
    lineas = len(datos) # Obtenemos las filas
    municipios_con_mar = 0

    for i in range(lineas):
        # Para trabajar con float se usa "."
        km_costa = float(datos[i][2].replace(",", "."))
        if (km_costa > 0):
            municipios_con_mar += 1

    return municipios_con_mar

def calcular_municipios_mas15k(datos: list[str]):
    lineas = len(datos)
    municipios_mas15k = 0

    for i in range(lineas):
        numero_hab = int(datos[i][7])
        if(numero_hab > 15000):
            municipios_mas15k += 1

    return municipios_mas15k

def calcular_playas(datos: list[str]):
    lineas = len(datos)
    num_playas = 0

    for i in range(lineas):
        playas = int(datos[i][3])
        num_playas += playas

    return num_playas

def calcular_hab_municipios_costeros(datos: list[str]):
    lineas = len(datos)
    num_hab = 0

    for i in range(lineas):
        km_costas = float(datos[i][2].replace(",", "."))
        hab = int(datos[i][7])
        if(km_costas > 0):
            num_hab += hab

    return num_hab

def calcular_hab_municipios_menos5k(datos: list[str]):
    lineas = len(datos)
    num_hab = 0

    for i in range(lineas):
        hab = int(datos[i][7])
        if(hab < 5000):
            num_hab += hab

    return num_hab

def calcular_km_costa_total(datos: list[str]):
    lineas = len(datos)
    km_costa_total = 0

    for i in range(lineas):
        km_costa_total += float(datos[i][2].replace(",", "."))

    return km_costa_total

def calcular_viviendas_costas(datos: list[str]):
    lineas = len(datos)
    viviendas_totales_costa = 0

    for i in range(lineas):
        km_costa = float(datos[i][2].replace(",", "."))
        viviendas = int(datos[i][4])
        if(km_costa > 0):
            viviendas_totales_costa += viviendas

    return viviendas_totales_costa

def calcular_densidad_poblacion_costa(datos: list[str]):
    lineas = len(datos)
    viviendas_totales = 0
    habitantes_totales = 0

    for i in range(lineas):
        km_costa = float(datos[i][2].replace(",", "."))
        viviendas = int(datos[i][4])
        habitantes = int(datos[i][7])
        if(km_costa > 0):
            viviendas_totales += viviendas
            habitantes_totales += habitantes

    return round(viviendas_totales / habitantes_totales, 2)

def calcular_densidad_poblacion(datos: list[str]):
    lineas = len(datos)
    viviendas_totales = 0
    habitantes_totales = 0
    
    for i in range(lineas):
        km_costa = float(datos[i][2].replace(",", "."))
        viviendas = int(datos[i][4])
        habitantes = int(datos[i][7])
        if(km_costa == 0):
            viviendas_totales += viviendas
            habitantes_totales += habitantes
    
    return round(viviendas_totales / habitantes_totales, 2)

soluciones_algoritmo = [
    ["Municipios con mar", calcular_municipios_mar(datos_leidos)],
    ["Municipios con más de 15000 habitantes", calcular_municipios_mas15k(datos_leidos)],
    ["Número de playas totales", calcular_playas(datos_leidos)],
    ["Número de habitantes totales en municipios costeros", calcular_hab_municipios_costeros(datos_leidos)],
    ["Número de habitantes totales en municipios con menos de 5000 habitantes", calcular_hab_municipios_menos5k(datos_leidos)],
    ["Número de km totales de costa en la provincia", calcular_km_costa_total(datos_leidos)],
    ["Número de viviendas totales en costas", calcular_viviendas_costas(datos_leidos)],
    ["Densidad de población en municipios costeros", calcular_densidad_poblacion_costa(datos_leidos)],
    ["Densidad de población en municipios no costeros", calcular_densidad_poblacion(datos_leidos)]
]

# Crea el archivo resultado.csv y escribe en él:
with open(ruta + "/resultado.csv", mode="w") as resultado:
    # Recorrer arrays bidimensionales: https://snakify.org/es/lessons/two_dimensional_lists_arrays/
    for i in range(len(soluciones_algoritmo)):
        for j in range(len(soluciones_algoritmo[i])):
            # Problema con soluciones_algoritmo, dice que es in???
            # https://stackoverflow.com/questions/52497195/typeerror-write-argument-must-be-str-not-int
            resultado.write(str(soluciones_algoritmo[i][j]) + "\t")
        resultado.write("\n")

# Crea el archivo soluciones.csv
# Soluciones al ejercicio
solucion = [
    ["Municipios con mar", 23],
    ["Municipios con más de 15000 habitantes", 29],
    ["Número de playas totales", 44],
    ["Número de habitantes totales en municipios costeros", 1021343],
    ["Número de habitantes totales en municipios con menos de 5000 habitantes", 272640],
    ["Número de km totales de costa en la provincia", 110.90],
    ["Número de viviendas totales en costas", 331177],
    ["Densidad de población en municipios costeros", 0.32],
    ["Densidad de población en municipios no costeros", 0.30]
]
with open(ruta + "/soluciones.csv", mode="w") as solucionesCsv:
    for i in range(len(solucion)):
        for j in range(len(solucion[i])):
            solucionesCsv.write(str(solucion[i][j]) + "\t")
        solucionesCsv.write("\n")
        
print("Comprobacion 1:")

# Comprobar que todo está correcto
with open(ruta + "/resultado.csv", mode="r") as fichero_a_comprobar:
    contenido_a_comprobar = fichero_a_comprobar.readlines()
with open(ruta + "/soluciones.csv", mode="r") as fichero_soluciones:
    contenido_soluciones = fichero_soluciones.readlines()
 
errores = 0

for i in range(len(contenido_a_comprobar)):
        # rstrip elimina los espacios en blanco. Se comprueba que todo sea exactamente igual
        # https://es.stackoverflow.com/questions/399446/comparar-dos-ficheros-en-python
    if (contenido_soluciones[i].rstrip().find(contenido_a_comprobar[i].rstrip()) == -1):
            errores += 1

if (errores  > 0): 
        print("Los datos no coinciden. Número de errores: " + str(errores))
else:
        print("Los datos coinciden.")

## Debugger: https://stackoverflow.com/questions/4929251/how-to-step-through-python-code-to-help-debug-issues
# q para salir



# Planteamiento de lectura de las tablas con 2 columnas

print("Comprobacion 2:")
    
datos_comprobacion = list()
    
with open(ruta + "/resultado.csv", mode="r") as fichero_a_comprobar:
    contenido_a_comprobar = fichero_a_comprobar.readlines()
    for i in range(len(contenido_a_comprobar)):
        if(i > 0):
            registro = contenido_a_comprobar[i].replace('\n', '')
            datos_comprobacion.append(registro.split("\t"))   

    
datos_soluciones = list()
    
with open(ruta + "/soluciones.csv", mode="r") as fichero_soluciones:
    contenido_soluciones = fichero_soluciones.readlines()
    for i in range(len(contenido_soluciones)):
        if(i > 0):
            registro = contenido_soluciones[i].replace('\n', '')
            datos_soluciones.append(registro.split("\t"))
            
           
errores = 0

for i in range(len(datos_soluciones)):
        # rstrip elimina los espacios en blanco. Se comprueba que todo sea exactamente igual
        # https://es.stackoverflow.com/questions/399446/comparar-dos-ficheros-en-python
    if datos_comprobacion[i][1] != datos_soluciones[i][1]:
            errores += 1

if (errores  > 0): 
        print("Los datos no coinciden. Número de errores: " + str(errores))
else:
        print("Los datos coinciden.")
