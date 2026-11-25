"""
Actividad: Comparación simple entre dos números

Descripción:
Solicita dos números por teclado y evalúa mediante una estructura
condicional simple (if / else) cuál de los dos es mayor, mostrando
el resultado por consola.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

# Ejemplo con Python

numero1 = input("Introduce un numero: ")
numero2 = input("Introduce un segundo numero: ")

if (numero1 > numero2):
    print("El primer numero es el mayor")
else:
    print("El segundo numero es el mayor")

print("Programa terminado")
