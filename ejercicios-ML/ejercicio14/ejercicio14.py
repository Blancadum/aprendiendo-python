"""
Blanca de Uña Martín
"""

import random

numero_secreto = random.randint(1, 20)
intentos = 5
acertado = False

print("Adivina el número del 1 al 20 (tienes 5 oportunidades).")

for i in range(intentos):
    intento = int(input(f"Intento {i+1}: "))
    
    if intento < numero_secreto:
        print("El número que buscas es mayor")
    elif intento > numero_secreto:
        print("El número que buscas es menor")
    else:
        print(f"¡Enhorabuena, acertaste, es el número {numero_secreto}!")
        acertado = True
        break

if not acertado:
    print(f"¡Oh, lo siento, era el número {numero_secreto}!")
