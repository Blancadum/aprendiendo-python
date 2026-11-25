"""
Actividad: Comparativa entre if-elif-else y Match-Case

Descripción:
Demuestra cómo resolver la misma lógica de bifurcación mediante dos enfoques:
1. Estructura condicional clásica (if / elif / else).
2. Estructura moderna de coincidencia de patrones match / case (introducida en Python 3.10),
   destacando el uso del patrón comodín 'case _:'.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la terminal antes de ejecutar (usa 'clear' en Mac/Linux y 'cls' en Windows)
os.system("clear")

# ==============================================================================
# EJEMPLO: Comparación entre condicionales tradicionales (if-elif-else) y Match-Case
# Demuestra cómo resolver la misma lógica de bifurcación mediante dos enfoques:
# 1. Estructura clásica con if / elif / else.
# 2. Estructura moderna con match / case (introducida a partir de Python 3.10).
# ==============================================================================
# 1. Entrada y conversión de datos por teclado
# input() captura el valor introducido por el usuario como texto (string)
numero = input("Introduce 0 o 1: ")

# int() convierte la cadena de texto a un número entero para poder compararlo numéricamente
numero = int(numero)

# ==============================================================================
# FORMA 1: Estructura condicional clásica (if / elif / else)
# Evalúa expresiones booleanas secuencialmente de arriba a abajo.
# ==============================================================================
print("\n--- Resultado con if-elif-else ---")

if numero == 0:
    # Se ejecuta si la condición 'numero == 0' es verdadera (True)
    print("Has introducido un 0")
elif numero == 1:
    # Se ejecuta si la condición anterior fue falsa y 'numero == 1' es verdadera
    print("Has introducido un 1")
else:
    # Caso por defecto: se ejecuta si ninguna de las condiciones anteriores se cumplió
    print("No has introducido ni 0 ni 1")

# ==============================================================================
# FORMA 2: Estructura moderna Match-Case (Pattern Matching)
# Evalúa el valor de la variable frente a diferentes patrones predefinidos (case).
# Es el equivalente en Python al switch-case de otros lenguajes (C, Java, JavaScript).
# ==============================================================================
print("\n--- Resultado con match-case ---")

match numero:
    case 0:
# Se ejecuta si el valor de 'numero' coincide exactamente con 0
        print("Has introducido un 0")
    case 1:
# Se ejecuta si el valor de 'numero' coincide exactamente con 1
        print("Has introducido un 1")
    case _:
# El guion bajo (_) es el patrón comodín (wildcard / default):
# Captura cualquier otro valor no contemplado en los casos anteriores
        print("No has introducido ni 0 ni 1")
