"""
solicitar al usuario del 1 al 10 con range
    mostrar tabla de multiplicar de ese número
    5
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    ...
    5 x 10 = 50

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

tabla = int(input("Introduce un número de la tabla, del 1 al 10: "))

for numero in range(1, 11):
    print(f"{tabla} x {numero} = {tabla * numero}")
