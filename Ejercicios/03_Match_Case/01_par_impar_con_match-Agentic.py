"""
Solicitar un número entero
    y mostrar si es par o impar

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo3_Match_case
"""

numero = int(input("Introduce un número entero: "))

# cada caso es una función:

match numero % 2:
    case 0:
        print(f"El numero {numero} es par")
    case 1:
        print(f"El numero {numero} es impar")
