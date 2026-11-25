"""
Actividad: Eliminación de elementos en listas (método remove)

Descripción:
Explica el funcionamiento del método .remove() para eliminar elementos
en una lista, observando cómo solo elimina la primera ocurrencia y cómo
implementar algoritmos para depurar o filtrar múltiples apariciones de un valor.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os

edades = list([20, 41, 6, 18, 23, 10, 5, 18])

print(edades)       # Mostrará 20, 41, 6, 18, 23, 10, 5, 18
print("\n")

# Quitar elementos de un Array. Con REMOVE se elimina la primera
#       coinciencia que encuentre. Para ir eliminando mas de un valor
#       hay que repetir el proceso hasta que no quede ningún número

edades.remove(18)
print(edades)       # Mostrará 20, 41, 6, 23, 10, 5, 18
print("\n")
os.system("cls")

# Creacion de un array nuevo borrando valores del original
edades=[5, 3, 2, 5, 7, 1, 9, 5, 5, 3, 2, 5, 7, 1, 9, 5]
valor = 5
nuevo=list()
nuevo2 = list()

# Opcion 1 para recorrer el array
contador = 0
for indice, value in enumerate(edades):
    if (value != valor):
        nuevo.append(value)
    else:
        contador = contador + 1
        if (contador <= 3):
            nuevo.append(value)

# Opcion 2 para recorrer el array
contador = 0
for indice in range(len(edades)):
    if (edades[indice] != valor):
        nuevo2.append(edades[indice])
    else:
        contador = contador + 1
        if (contador <= 3):
            nuevo2.append(edades[indice])

print(edades)
print("\n")
print(nuevo)
print("\n")
print(nuevo2)
