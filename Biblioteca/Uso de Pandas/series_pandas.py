
        # Creación de listas o series con Pandas

        # Antes de empezar con Pandas hay que instalar la librería usando el terminal

        # Abrimos CMD o Powershell en modo administrador y ejecutamos:

        #               pip install pandas



import os

os.system('cls' if os.name == 'nt' else 'clear')

directorio_actual = os.path.dirname(os.path.abspath(__file__))
# fichero_csv = os.path.join(directorio_actual, "fichero.csv")

import pandas as pd         # Importamos la librería Pandas

import numpy as np          # Importamos la librería Numpy (no obligatorio)


# Creación de una lista básica. Es similar a los Arrays básicos o NumPy.

ejemplo_base = list()       # Crea una lista básica de Python

ejemplo_numpy = np.array()  # Crea un array vacio usando la libreria Numpy

ejemplo = pd.Series([])     # Crea un serie vacia usando la libreria Pandas


ejemplo = pd.Series([7,5,6,8,9,2,5], dtype='int')

ejemplo0 = pd.Series([7,5,6.3,8,9,2,5], dtype='float')

ejemplo1 = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')


print("\n")

print(ejemplo1)

print("\n")



# Podemos crear una lista asignándole un índice, numérico o texto.
# A estas series se les llama diccionario
# Para crear series de diccionarios se pueden usar llaves definiendo duplas indice:dato

ejemplo2 = pd.Series({'Matemáticas': 6.0, 'Economía': 4.5, 'Programación': 8.5}, dtype='float')


# También se pueden usar corchetes definiendo por un lado los datos y por otro los índices

ejemplo3 = pd.Series([6.0, 4.5, 8.5], dtype='float', index = ['Matemáticas', 'Economía', 'Programación'])

asignaturas = list(['Matemáticas', 'Economía', 'Programación'])

ejemplo3 = pd.Series([6.0, 4.5, 8.5], dtype='float', index = asignaturas)


longitud = len(ejemplo3)           # Devuelve cuantos elementos hay en la serie


# Localización de datos. Se puede usar por posicion n-1 o por el índice

print(ejemplo3[ejemplo3<7])        # Devuelve los valores menores de 7

print("\n")

print(ejemplo3[2])               # Devuelve el elemento situado en la posicion 3 --> 8.5

print("\n")

print(ejemplo3['Matemáticas'])    # Devuelve el valor del elemento situado en la posicion 'Matemáticas' --> 6.0

print("\n")


    # Es posible sacar datos con más de un índice a la vez

print(str(ejemplo3[2]) + " " + str(ejemplo3[0]))    # Devuelve los valores 8.5 y 6.0

print(ejemplo3[['Economía', 'Matemáticas']])        # Devuelve los valores 4.5 y 6.0

print("\n")



# Funciones que se aplican en listas o series de Pandas:

# count(): Devuelve el número de elementos que no son nulos ni NaN en la serie

print("En la serie hay " + str(ejemplo3.count()) + " datos no nulos")


# sum(): Devuelve la suma de los datos de la serie cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
# cumsum(): Devuelve una serie con la suma acumulada de los datos de la serie cuando los datos son de un tipo numérico.
# value_counts(): Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie original.
# min(): Devuelve el menor de los datos de la serie.
# max(): Devuelve el mayor de los datos de la serie.
# mean(): Devuelve la media de los datos de la serie cuando los datos son de un tipo numérico
# var(): Devuelve la varianza de los datos de la serie cuando los datos son de un tipo numérico.
# std(): Devuelve la desviación típica de los datos de la serie cuando los datos son de un tipo numérico.
# describe(): Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, 
#                       el máximo, la media, la desviación típica y los cuartiles.

media = round(ejemplo3.mean(), 2)

print(media)


print("\n")

print(ejemplo3.describe())

print("\n")

print(ejemplo3.describe()[4])

print("\n")


# Ordenación de series

# Para ordenar por los valores de la serie. 
    # Si ascending = True --> Orden creciente.
    # Si ascending = False --> Orden decreciente.

ordenado1 = ejemplo3.sort_values(ascending=True)

print(ordenado1)

print("\n")

# Para ordenar por los indices de la serie. 
    # Si ascending = True --> Orden creciente.
    # Si ascending = False --> Orden decreciente.


ordenado2 = ejemplo3.sort_index(ascending=False)

ejemplo3 = ejemplo3.sort_index(ascending=False)

print(ordenado2)

print("\n")


# Importacion basica de datos desde un fichero .csv

# ejemplo4 = pd.read_csv("fichero.csv", sep=";", dtype="string", header="none")


    # Parámetros que se le pueden añadir:
    # sep="separador"       --- Si no se define toma por defecto la coma
    # dtype="tipo de dato"  --- Si no se define por defecto toma numeros enteros
    # header=none           --- Podemos elegir tomar la cabecera del documento o no