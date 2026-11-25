"""
Calculadora mejorada:
    - Solicitar 2 números reales.
    - Solicitar qué operación: +, -, *, /
    - Mostrar resultado

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo2_Condicionales
"""

num1 = float(input("Introduce un primer numero: "))
num2 = float(input("Introduce un segundo numero: "))
operacion = input("Introduce qué operación quieres ejecutar: +, -, * o /: ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
else:
    resultado = "Operación no válida"

print(resultado)
