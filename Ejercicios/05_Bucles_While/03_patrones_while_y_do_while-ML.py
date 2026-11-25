"""
Actividad: Estructura del bucle while y simulación de do-while

Descripción:
Explica las diferencias entre bucles finitos (for) e indeterminados (while).
Muestra tres patrones para validar la entrada de un número par distinto de cero:
lectura anticipada, bandera de control y el patrón estándar 'while True' con 'break'.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

# Los bucles son partes del programa que se repiten
# Podemos encontrarnos con dos tipos de bucles:
# - Los bucles finitos o determinados: aquellos que se repiten un número fijo de veces. Se construyen con FOR.
# - Los bucles no finitos o indeterminados: aquellos que se repiten un número variable de veces. Se construyen con WHILE.
# 1. Ejemplo básico con WHILE (Lectura anticipada)
numero = int(input("Introduce un numero par distinto de cero: "))
resto = numero % 2

while (numero == 0) or (resto != 0):
    print("No has escrito un numero correcto")
    numero = int(input("Introduce un numero par distinto de cero: "))
    resto = numero % 2

print("El numero " + str(numero) + " es par y distinto de cero.\n")

# 2. Equivalencia a DO..WHILE (con variable de control)
control = True
while control:
    numero = int(input("Introduce un numero par distinto de cero: "))
    resto = numero % 2
    if (numero == 0) or (resto != 0):
        print("No has escrito un numero correcto")
    else:
        control = False

print("El numero " + str(numero) + " es par y distinto de cero.\n")

# 3. Otra equivalencia de DO..WHILE (con while True y break)
while True:
    numero = int(input("Introduce un numero par distinto de cero: "))
    resto = numero % 2
    if (numero == 0) or (resto != 0):
        print("No has escrito un numero correcto")
    else:
        break

print("El numero " + str(numero) + " es par y distinto de cero.")
