"""
Actividad: Calificación académica con if-elif-else anidados

Descripción:
Clasifica la nota de un alumno en Sobresaliente (>= 9), Notable (>= 7),
Bien (>= 6), Suficiente (>= 5), Insuficiente (>= 3) o Muy Deficiente (< 3)
utilizando una estructura encadenada if / elif / else.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

nota = input("Introduce una nota: ")
nota = float(nota)

if(nota >= 9):
    print("El alumno ha sacado un SOBRESALIENTE")

    # elif = else if: permite agregar un condicional dentro de otro condicional
elif(nota >= 7):
    print("El alumno ha sacado un NOTABLE")
elif(nota >= 6):
    print("El alumno ha sacado un BIEN")
elif(nota >= 5):
    print("El alumno ha sacado un SUFICIENTE")
elif(nota >= 3):
    print("El alumno ha sacado un INSUFICIENTE")
else:
    print("El alumno ha sacado un MUY DEFICIENTE")
