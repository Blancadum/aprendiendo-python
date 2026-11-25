"""
Actividad: Precedencia y evaluación de operadores lógicos (OR y AND)

Descripción:
Ejemplo práctico que analiza el orden de evaluación y precedencia de los
operadores lógicos 'and' y 'or' en Python aplicados a la autenticación de credenciales.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

usuario = "Pepito"
clave = "A1234b"

usuarionew = input("Escribe el usuario: ")
clavenew = input("Escribe la contraseña: ")
dato = input("Escribe algo: ")

# or permite evaluar dos o mas condiciones y determinar si al menos una de ellas es válida
# and permite evaluar dos o mas condiciones y determinar si TODAS son válidas
#0                  *        0               +      1

if(usuarionew == "Pepito") and (clavenew == "A1234b") or (dato != ""):
    print("Has acertado el usuario y la contraseña")
else:
    print("No has acertado alguna de la palabras")
