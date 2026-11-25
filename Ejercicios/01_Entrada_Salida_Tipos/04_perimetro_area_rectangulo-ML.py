"""
Ejercicio 02: Cálculo del perímetro y área de un rectángulo

Descripción:
Escribe un programa que pregunte al usuario los dos lados de un rectángulo
y presente por pantalla el cálculo del perímetro (suma de los lados)
y el área (base por altura) redondeando a dos decimales.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 02.- Cálculo del perímetro y área de un rectángulo
# Programa que solicita al usuario la longitud de los dos lados de un rectángulo
# y calcula tanto su perímetro como su área, mostrando los resultados con dos decimales.

# 1. Solicitar los lados al usuario convirtiéndolos a tipo float
# Usamos float() para permitir que el usuario introduzca números decimales
lado1 = float(input("Introduce el primer lado del rectángulo: "))
lado2 = float(input("Introduce el segundo lado del rectángulo: "))

# 2. Realizar los cálculos geométricos
# El perímetro es la suma de todos los lados: 2 * (base + altura)
perimetro = 2 * (lado1 + lado2)

# El área es la multiplicación de la base por la altura
area = lado1 * lado2

# 3. Mostrar los resultados por terminal con formato de dos decimales
# Usamos :.2f dentro de la f-string para formatear los números a dos cifras decimales
print()
print("--- RESULTADOS ---")
print(f"Perímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")
