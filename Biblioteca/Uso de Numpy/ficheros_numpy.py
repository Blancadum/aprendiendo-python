
           # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

carpeta = ""
fichero = "base_coches.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import numpy as np

# Cargar datos desde un fichero

nuevo = np.loadtxt(carpeta + fichero, dtype=str, delimiter="\t") 

os.system("cls")

print(nuevo)

print()

        # Si no le indicamos el tipo de dato, por defecto toma tipo float
        # Si no le indicamos el delimitador, por defecto toma el espacio


# Para imprimir los valores de la tabla usando tabulaciones

filas = len(nuevo)

if filas > 0:
    columnas = len(nuevo[0])

    for i in range(filas):
        linea=""
        for j in range(columnas):
            linea = linea + str(nuevo[i][j]) + "\t"
        print (linea)

print("\n\n")



# Para descartar filas a importar usamos skiprows.
# Por ejemplo, podemos descartar las primeras 2 filas.
    

nuevo = np.loadtxt(carpeta + fichero, skiprows=2, dtype=str, delimiter="\t") 

filas = len(nuevo)

if filas > 0:
    columnas = len(nuevo[0])

    for i in range(filas):
        linea=""
        for j in range(columnas):
            linea = linea + str(nuevo[i][j]) + "\t"
        print (linea)

print("\n\n")



# Para importar columnas concretas usamos usecols.
# Por ejemplo, podemos importar solo las columnas de marca, modelo y matricula.
    
nuevo = np.loadtxt(carpeta + fichero, usecols=(0,1,4), dtype=str, delimiter="\t") 

filas = len(nuevo)

if filas > 0:
    columnas = len(nuevo[0])

    for i in range(filas):
        linea=""
        for j in range(columnas):
            linea = linea + str(nuevo[i][j]) + "\t"
        print (linea)

print("\n\n")

# Para guardar una tabla de NumPy en un fichero de texto

np.savetxt(carpeta + "prueba.csv", nuevo, delimiter=';', fmt=['%s','%s','%s'])

