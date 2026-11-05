

import random

import os

os.system("cls")

# Genera un número array aleatorio entre 1 y 10 (inclusive)


valores = list()

for i in range(10):
    
    numero = 0
    
    while numero == 0:
        numero = random.randint(-100, 100)
    
    valores.append(numero)

print(valores)                  # Imprimimos el array en horizontal

print()

for i in valores:               # Imprimimos el array en vertical
    print(i)

print()

for i in range(len(valores)):   # Imprimimos el array en vertical
    print(valores[i])