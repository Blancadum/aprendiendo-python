"""
Mostrar las 10 tablas de multiplicar
    2 bucles
    1º es el que recorre las tablas
    2º es el que recorre los números de la tabla

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

# 1º bucle: recorre cada tabla del 1 al 10
for tabla in range(1, 11):
    print(f"\n--- Tabla del {tabla} ---")

    # 2º bucle: recorre los números a multiplicar del 1 al 10
    for numero in range(1, 11):
        print(f"{tabla} x {numero} = {tabla * numero}")
