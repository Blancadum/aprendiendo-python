"""
Actividad: Estructura del bucle for, rangos y resolución de patrones

Descripción:
Explica la diferencia entre bucles determinados (for) e indeterminados (while).
Demuestra el uso de la función range() con paso ascendente y descendente (cuenta regresiva).
Incluye la resolución práctica de validación de entrada mediante while para solicitar
un número positivo mayor que cero e imprimir una fila de N asteriscos con for.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

# Los bucles son partes del programa que se repiten
# Podemos encontrarnos con dos tipos de bucles:
# - Los bucles finitos o determinados: aquellos que se repiten un número fijo de veces. Se construyen con FOR.
# - Los bucles no finitos o indeterminados: aquellos que se repiten un número variable de veces. Se construyen con WHILE.
# for (i=10; i>0; i--){ alert(i); }
for i in range(10):
    print(i)

print("")

for i in range(10, 0, -1):
    print(i)

# Resolución del ejercicio 11
os.system("cls")

valor = 0
texto = ""

while valor <= 0:
    valor = int(input("Escribe un numero entero positivo mayor que cero: "))

for i in range(valor):
    texto = texto + "* "

print(texto)
