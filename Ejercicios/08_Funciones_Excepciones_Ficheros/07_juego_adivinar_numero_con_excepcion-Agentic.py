"""
Enunciado:
Juego de adivinar un número con gestión de excepciones:
1. Generar un número aleatorio del 1 al 10.
2. Solicitar iterativamente al usuario que lo adivine, ofreciendo pistas
   ("Te has quedado corto" o "Te has pasado").
3. Controlar mediante try / except que si el usuario introduce un texto no numérico,
   el programa capture el ValueError y muestre un mensaje de advertencia sin detener la ejecución.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 11_Excepciones
"""

import random

numero_secreto = random.randint(1, 10)
adivinar = 0

print("--- JUEGO: ADIVINA EL NÚMERO (1 - 10) ---")

while adivinar != numero_secreto:
    try:
        entrada = input("Adivina el número: ")
        adivinar = int(entrada)

        if adivinar < numero_secreto:
            print("Te has quedado corto, vuelve a intentarlo.")
        elif adivinar > numero_secreto:
            print("Te has pasado, vuelve a intentarlo.")
        else:
            print("¡Enhorabuena, lo adivinaste!")

    except ValueError:
        print("Error: Debes introducir un número entero válido (del 1 al 10).\n")
