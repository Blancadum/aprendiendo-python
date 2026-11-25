"""
Solicitar un número al usuario, mostrar desde el 0 hasta ese número, solo los pares
8 -> 0, 2, 4, 6, 8
11 -> 0, 2, 4, 6, 8, 10
con bucle while

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo6_password
"""

numero = int(input("Introduce un número: "))
num = 0
while num <= numero:
    if num % 2 == 0:
        print(num)
    num += 1
