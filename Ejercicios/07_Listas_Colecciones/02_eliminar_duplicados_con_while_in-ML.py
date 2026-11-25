"""
Actividad: Eliminación de todas las repeticiones de un valor en una lista

Descripción:
Muestra cómo eliminar de forma exhaustiva todas las coincidencias de un
elemento específico dentro de una lista utilizando un bucle while junto
con el operador de pertenencia 'in' y el método .remove().

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

# Creacion de un array nuevo borrando valores del original

edades=[5, 3, 2, 5, 7, 1, 9, 5, 5, 3, 2, 5, 7, 1, 9, 5]

valor = 5       # Numero a eliminar del array

print("Array con el 5 sin borrar")
print(edades)

# Opcion 1

while True:
    if valor in edades:
        edades.remove(valor)
    else:
        print("Se ha eliminado el numero " + str(valor))
        break

# Opcion 2

while valor in edades:
        edades.remove(valor)
else:
    print("Se ha eliminado el numero " + str(valor))

print("\nArray con el 5 borrado")
print(edades)

# Usando una funcion

def borrado_total(valor):
    while valor in edades:
        edades.remove(valor)
    else:
        print("Se ha eliminado el numero " + str(valor))

for i in range(18):
    borrado_total(i)

for i in range(66,121,1):
    borrado_total(i)

edades.remove(valor)
