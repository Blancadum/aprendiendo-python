"""
Solicitar un número al usuario y mostrar su factorial
    5
    5 x 4 x 3 x 2 x 1

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

numero = int(input("Introduce un número entero: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es {factorial}")
