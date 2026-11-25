"""
Actividad: Operadores lógicos compuestos (AND / OR)

Descripción:
Demuestra la validación de credenciales (usuario y contraseña) combinando
los operadores lógicos 'and' (conjunción) y 'or' (disyunción) para evaluar
múltiples condiciones booleanas en una sola expresión.

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
#0                  *        0               +     1

if(usuarionew == usuario) and (clavenew == clave) or (dato != ""):
    print("Has acertado el usuario y la contraseña")
else:
    print("No has acertado alguna de la palabras")
