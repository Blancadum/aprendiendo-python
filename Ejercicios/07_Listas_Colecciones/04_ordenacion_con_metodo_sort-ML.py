"""
Actividad: Manipulación, tipado y ordenación de listas (método sort)

Descripción:
Demuestra la normalización de elementos de una lista mixta convirtiéndolos a texto
capitalizado con .capitalize(), modificación por índice y posterior ordenación
alfabética utilizando el método .sort().

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

textos = ["Hola", 4 , 5 , 0 , "adios"]

for i in range(len(textos)):
    textos[i] = str(textos[i]).capitalize()

textos[2] = 27

copia = list()

for i in range(len(textos)):
    copia.append(str(textos[i]).capitalize())

copia.sort()

print(textos)
print("")
print(copia)

# Ordenar un array de menor a mayor

numeros = [4, 1, 3, 2]
numeros.sort()
print(numeros)  # [1, 2, 3, 4]

# Ordenar un array de menor a mayor guardando original

numeros = [5, 2, 9, 1]
ordenados = sorted(numeros)
# Resultado: [1, 2, 5, 9]
# Ordenar un array de mayor a menor

mi_lista = [1, 2, 3, 4, 5]
mi_lista.reverse()

print(mi_lista)  # Salida: [5, 4, 3, 2, 1]

numeros = [4, 1, 3, 2]
numeros.sort(reverse=True)
print(numeros)  # [4, 3, 2, 1]

# Ejemplos de ordenacion

numeros = [5, 2, 9, 1]
descendente = sorted(numeros, reverse=True)
# Resultado: [9, 5, 2, 1]
#### Uso del parámetro `key` (por longitud de cadena)

palabras = ["manzana", "sol", "elefante"]
por_tamano = sorted(palabras, key=len)
# Resultado: ['sol', 'manzana', 'elefante']

palabras = ["manzana", "sol", "elefante"]
por_tamano = sorted(palabras, key=len, reverse=True)
# Resultado: ['elefante', 'manzana', 'sol']
