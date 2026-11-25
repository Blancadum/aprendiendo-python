"""
Ejercicio 15: Generación y recorrido de listas con números aleatorios

Descripción:
Genera una lista con 10 números enteros aleatorios en el rango de -100 a 100
(excluyendo el cero). Muestra la lista en horizontal y posteriormente
en vertical utilizando dos métodos de recorrido: directo por elemento y por índice.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de librerías del sistema y generación de números aleatorios
import os
import random

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
os.system("clear")

# Ejercicio 15.- Generación y recorrido de listas de números aleatorios
# Programa que crea una lista con 10 números aleatorios entre -100 y 100 (excluyendo el 0),
# y la muestra tanto de forma horizontal como vertical (por elemento y por índice).

# 1. Inicialización de la lista vacía
valores = list()

# 2. Generación de 10 números aleatorios no nulos
for i in range(10):
    numero = 0
    # Bucle while para garantizar que ningún número sea 0
    while numero == 0:
        numero = random.randint(-100, 100)
    valores.append(numero)

# 3. Mostrar la lista completa en horizontal
print("=== LISTA EN HORIZONTAL ===")
print(valores)
print()

# 4. Recorrido vertical directamente por elemento
print("=== LISTA EN VERTICAL (POR ELEMENTO) ===")
for elemento in valores:
    print(elemento)
print()

# 5. Recorrido vertical mediante índices con range(len(valores))
print("=== LISTA EN VERTICAL (POR ÍNDICE) ===")
for i in range(len(valores)):
    print(f"Índice [{i}]: {valores[i]}")
