"""
Actividad: Evaluación de notas con condicional simple

Descripción:
Pide una calificación numérica (tipo float) y determina mediante una
estructura if / else si el alumno está aprobado (nota >= 5) o suspenso.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

# nota=float(input("Introduce una nota: "))

nota = input("Introduce una nota: ")
nota = float(nota)

if(nota >= 5):
    print("El alumno esta aprobado")
else:
    print("El alumno esta suspenso")
