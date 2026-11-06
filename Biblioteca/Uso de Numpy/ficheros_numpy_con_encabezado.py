
           # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

carpeta = ""
fichero = "base_coches.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import numpy as np

# Cargar datos desde un fichero

nuevo = np.loadtxt(carpeta + fichero, dtype=str, delimiter="\t") 

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


# Para incorporar encabezados. Primero creamos una tabla nueva con el encabezado

cabecera = np.array([["Marca","Modelo", "Año", "Color", "Matricula"]])


completo = np.concatenate((cabecera, nuevo), axis=0)


np.savetxt(carpeta + "concabecera.csv", completo, delimiter=';', fmt=['%s','%s','%s','%s','%s'])

input("Pulse enter para continuar")
os.system("cls")

# Duplicar un array y ver sus parametros

copia = np.copy(completo)

filas = len(copia)
columnas = len(copia[0])

# Podemos usar shape para saber los parametros de la tabla

filas = copia.shape[0]
columnas = copia.shape[1]

dimension = copia.ndim
dimension = len(copia.shape)

# Para imprimir los valores de la tabla usando tabulaciones


filas = len(nuevo)

if filas > 0:
    columnas = len(nuevo[0])

    for i in range(filas):
        linea=""
        for j in range(columnas):
            linea = linea + str(copia[i][j]) + "\t"
        print (linea)

print("\n\n")


print("Sus parámetros son: " + str(copia.shape))
print("Su dimension es: " + str(len(copia.shape)))
print("Es decir, tiene " + str(copia.shape[0]-1) + " filas de datos")   # Número de filas
print("Y tiene " + str(copia.shape[1]) + " columnas")                   # Número de columnas

