
           # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

from os import system
system("cls")

carpeta = ""
fichero = "base_coches.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import numpy as np

# Cargar datos desde un fichero

nuevo = np.loadtxt(carpeta + fichero, dtype=str, delimiter="\t") 

                # Si no le indicamos el tipo de dato, por defecto toma tipo float
                # Si no le indicamos el delimitador, por defecto toma el espacio


# Para imprimir los valores de la tabla usando tabulaciones

filas = len(nuevo)
columnas = len(nuevo[0])

for i in range(filas):
    linea=""
    for j in range(columnas):
        linea = linea + str(nuevo[i][j]) + "\t"
    print (linea + "\n")

print("\n")


                # Métodos especiales de los Arrays de NumPy


print("El array tiene " + str(nuevo.size) + " elementos")   # Numero de elementos del array (filas * columnas)

print("Tiene " + str(nuevo.ndim) + " dimensiones")          # Numero de dimensiones del array 

print("Sus parámetros son " + str(nuevo.shape))             # Numero de filas y columnas del array

print("Es decir, tiene " + str(nuevo.shape[0]) + " filas")  # Numero de filas

print("Y tiene " + str(nuevo.shape[1]) + " columnas")       # Numero de columnas

print("\n\n")


            # Para crear una copia del array de NumPy

copia = np.copy(nuevo)  

            # Para modificar un array de NumPy

copia[0,0]="HOLA"
copia[0,1]="ESTO"
copia[0,2]="ES"
copia[0,3]="UNA"
copia[0,4]="COPIA"

    # Imprimiendo el array copia en el terminal usando métodos de NumPy

for i in range(copia.shape[0]):
    linea=""
    for j in range(copia.shape[1]):
        linea = linea + str(copia[i][j]) + "\t"
    print (linea + "\n")

print("\n\n\n")



# Operaciones básicas en arrays de 2 dimensiones
# Siendo nombre el nombre de la tabla de NumPy



nombre = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


recorre = nombre.shape

filas = len(nombre)

columnas = len(nombre[0])

filas = recorre[0]

columnas = recorre[1]


print(nombre)

media = np.mean(nombre, dtype=np.float64)           # Media de todos los valores de la matriz

mediacol = np.mean(nombre[:, 2], dtype=np.float64)  # Media de la columna 3

mediafil = np.mean(nombre[0, :], dtype=np.float64)  # Media de la fila 1


print("\nMedia de la matriz:\t" + str(media))

print("Media de la columna 3:\t" + str(mediacol))

print("Media de la fila 1:\t" + str(mediafil))


# Para calcular medias parciales en filas o columnas

media_parcial_col = np.mean(nombre[1:3, 2], dtype=np.float64)  # Media de la columna 2, solo de las filas 2 y 3

media_parcial_fil = np.mean(nombre[0, 1:3], dtype=np.float64)  # Media de la fila 1, solo de las columnas 2 y 3

print("\nMedia parcial de la columna 3, solo filas 2 y 3: "+ str(media_parcial_col))

print("\nMedia parcial de la fila 1, solo columnas 2 y 3: "+ str(media_parcial_fil))



print("\n")

# Desviación estándar y varianza

desv_estandar = np.std(nombre, dtype=np.float64)            # Desviacion estándar de toda la tabla

varianza = np.var(nombre, dtype=np.float64)                 # Varianza de toda la tabla

desv_std_col = np.std(nombre[:, 2], dtype=np.float64)       # Desviación estándar columna 3

varianza_fila = np.var(nombre[0, :], dtype=np.float64)      # Varianza por fila 1


# Mínimos y máximos

minimo = nombre.min()               # Valor mínimo de toda la tabla

maximo = nombre.max()               # Valor máximo de toda la tabla

minimo_col = nombre[:, 2].min()     # Mínimo por columna 3

maximo_fila = nombre[0, :].max()    # Máximo por fila 1


# Suma y producto de los elementos, suma y producto acumulativos

suma = np.sum(nombre, dtype=np.float64)

producto = np.prod(nombre, dtype=np.float64)

# Suma acumulativa. Recorre por filas.

suma_fila = np.cumsum(nombre, dtype=np.float64)

# Producto acumulativo. Recorre por filas.

prod_fila = np.cumprod(nombre, dtype=np.float64)
