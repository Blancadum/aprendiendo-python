"""
Ejercicio 04: Operaciones aritméticas y precedencia de operadores

Descripción:
Escribir un programa que calcule y muestre por pantalla el resultado
de la siguiente operación aritmética redondeando a dos decimales:
    ((3 + 2) / (2 * 5)) ** 2

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 04.- Operaciones aritméticas y precedencia de operadores
# Escribir un programa que calcule y muestre por pantalla el resultado
# de la expresión: ((3 + 2) / (2 * 5)) ** 2 redondeando a dos decimales.

# 1. Cálculo de la expresión matemática respetando la jerarquía de operadores:
# - Primero se resuelven los paréntesis interiores: (3 + 2 = 5) y (2 * 5 = 10)
# - Luego la división: 5 / 10 = 0.5
# - Finalmente la potencia al cuadrado mediante el operador '**': 0.5 ** 2 = 0.25
resultado = ((3 + 2) / (2 * 5)) ** 2

# 2. Mostrar el resultado por pantalla
# round(resultado, 2) asegura que el valor se presente con un máximo de 2 decimales
print("--- RESULTADO DE LA OPERACIÓN ---")
print(f"El resultado es: {round(resultado, 2)}")
