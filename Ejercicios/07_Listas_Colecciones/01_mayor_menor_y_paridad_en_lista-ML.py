"""
Ejercicio 06: Mayor, menor y paridad de tres números

Descripción:
Realizar un programa que pida al usuario tres números enteros y determine
cuál es el mayor y cuál el menor. Además, analiza cada uno de los números
para indicar si son pares o impares.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 06.- Comparación de tres números y comprobación de paridad
# Programa que solicita tres números enteros al usuario, determina cuál es el mayor,
# cuál es el menor, y analiza la paridad (par o impar) de cada uno de ellos.

# 1. Solicitar los tres números por pantalla usando int(input())
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# 2. Agrupar los números en una lista para facilitar su tratamiento
numeros = [num1, num2, num3]

# 3. Identificar el mayor y menor mediante las funciones integradas max() y min()
mayor = max(numeros)
menor = min(numeros)

print()
print("--- RESULTADOS ---")
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")
print()

# 4. Determinar si cada número es par o impar recorriendo la lista con un bucle for
# El operador módulo '%' calcula el resto de la división entre 2; si es 0, el número es par
for n in numeros:
    if n % 2 == 0:
        print(f"El número {n} es par.")
    else:
        print(f"El número {n} es impar.")
