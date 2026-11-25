"""
Ejercicio 11: Impresión de patrones en bucle

Descripción:
Solicita al usuario una cantidad entera de asteriscos e imprime esa misma
cantidad en una sola línea horizontal continua utilizando un bucle for.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 11.- Impresión de patrones en bucle for
# Programa que pide al usuario una cantidad e imprime esa misma cantidad
# de asteriscos seguidos en una sola línea horizontal.

# 1. Solicitar la cantidad de asteriscos al usuario
cantidad = int(input("¿Cuántos asteriscos desea imprimir?: "))

# 2. Bucle for con range() para iterar 'cantidad' veces
# Usamos end="" en print() para evitar el salto de línea automático
print()
print("Resultado:")
for i in range(cantidad):
    print("*", end="")

# 3. Salto de línea final para separar la salida de la terminal
print()
