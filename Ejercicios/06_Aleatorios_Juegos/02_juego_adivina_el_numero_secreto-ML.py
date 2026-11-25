"""
Ejercicio 14: Juego de adivinar el número secreto

Descripción:
El programa genera un número aleatorio entre 1 y 20 con el módulo random.
El usuario dispone de 5 intentos para acertarlo, recibiendo pistas
de si el número buscado es mayor o menor tras cada intento fallido.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de librerías para utilidades del sistema y números aleatorios
import os
import random

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
os.system("clear")

# Ejercicio 14.- Juego: Adivina el número secreto
# El ordenador genera un número aleatorio entre 1 y 20 con random.randint().
# El usuario dispone de 5 intentos para adivinarlo, recibiendo pistas
# de si el número buscado es mayor o menor en cada ronda.

# 1. Generar el número secreto e inicializar variables de control
numero_secreto = random.randint(1, 20)
intentos_totales = 5
acertado = False

print("=== JUEGO: ADIVINA EL NÚMERO SECRETO ===")
print("He pensado un número del 1 al 20. ¡Tienes 5 oportunidades para adivinarlo!")
print()

# 2. Bucle for para gestionar los 5 intentos del jugador
for i in range(intentos_totales):
    intento = int(input(f"Intento {i + 1} de {intentos_totales}: "))

    # Comprobación y pistas
    if intento < numero_secreto:
        print("-> El número que buscas es MAYOR.")
        print()
    elif intento > numero_secreto:
        print("-> El número que buscas es MENOR.")
        print()
    else:
        print()
        print(f"🎉 ¡Enhorabuena, acertaste! El número secreto era el {numero_secreto}!")
        acertado = True
        break  # Se interrumpe el bucle al haber acertado

# 3. Mensaje en caso de agotar los intentos sin acertar
if not acertado:
    print()
    print(f"😢 ¡Oh, lo siento! Agotaste tus 5 intentos. El número secreto era el {numero_secreto}.")
