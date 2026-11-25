"""
Ejercicio 13: Filtrado de números pares o impares en un rango

Descripción:
Pide dos números enteros (definiendo un rango entre el menor y el mayor)
y una opción ('p' para pares o 'i' para impares). Recorre el intervalo inclusivo
mostrando únicamente los números que cumplan el criterio seleccionado.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 13.- Filtrado de números pares o impares en un rango
# Solicita dos números enteros al usuario y una letra:
# - 'p' para mostrar los números pares del rango.
# - 'i' para mostrar los números impares del rango.

# 1. Captura de los números y la opción deseada
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
letra = input("Introduce 'p' para pares o 'i' para impares: ").lower()

# 2. Determinar el inicio y el fin del rango independientemente del orden de entrada
inicio = min(num1, num2)
fin = max(num1, num2)

# 3. Recorrer el intervalo inclusivo (desde inicio hasta fin inclusive: fin + 1)
print()
print(f"--- NÚMEROS FILTRADOS EN EL RANGO [{inicio}, {fin}] ---")
if letra == 'p':
    # Si el resto de dividir entre 2 es 0, es número par
    for i in range(inicio, fin + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

elif letra == 'i':
    # Si el resto de dividir entre 2 es distinto de 0, es número impar
    for i in range(inicio, fin + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

else:
    print("Opción no válida. Debes introducir 'p' o 'i'.")
