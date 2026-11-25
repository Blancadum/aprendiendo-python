"""
Actividad: Evaluación con múltiples if independientes

Descripción:
Ejemplo didáctico que ilustra el comportamiento de utilizar varios bloques 'if'
independientes consecutivos para categorizar una nota, mostrando la diferencia
con respecto al uso de estructuras 'elif'.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

nota = input("Introduce una nota: ")
nota = float(nota)

if(nota >= 9):
    print("El alumno ha sacado un SOBRESALIENTE")

if(nota >= 7):
    print("El alumno ha sacado un NOTABLE")

if(nota >= 6):
    print("El alumno ha sacado un BIEN")

if(nota >= 5):
    print("El alumno ha sacado un SUFICIENTE")

if(nota >= 3):
    print("El alumno ha sacado un INSUFICIENTE")

if(nota >= 0):
    print("El alumno ha sacado un MUY DEFICIENTE")
