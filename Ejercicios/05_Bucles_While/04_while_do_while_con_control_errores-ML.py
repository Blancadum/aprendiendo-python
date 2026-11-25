"""
Actividad: Bucle de validación con captura de excepciones (try / except)

Descripción:
Combina un bucle 'while True' de simulación do-while con un bloque
'try - except' para blindar la entrada de datos frente a errores de tipo
(ValueError si el usuario introduce letras en vez de números enteros).

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
os.system("cls")

# Simulación de DO..WHILE con control de excepciones (try/except)
while True:
    try:
        numero = int(input("Introduce un numero positivo par distinto de cero: "))
        resto = numero % 2

        if (numero <= 0) or (resto != 0):
            print("No has escrito un numero correcto")
        else:
            break
    except ValueError:
        print("No has escrito un valor válido, repítelo")

print("El numero " + str(numero) + " es positivo, par y distinto de cero.")
