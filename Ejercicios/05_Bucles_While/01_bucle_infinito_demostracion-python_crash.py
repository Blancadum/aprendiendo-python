"""
Ejercicio 7-7: Demostración de bucle infinito controlado

Enunciado:
Demostración didáctica de un bucle while True infinito con temporizador de pausa (time.sleep).

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

# This program demonstrates a truly infinite loop.
# The program imports time to enter a small delay because we don't want it to flood the console

import time
print("Starting infinite loop (press Ctrl+C to stop)...")

while True: # The condition is always True, so the loop never ends
    print("This message will print forever!")
    time.sleep(0.5) # waits for 0.5 seconds
