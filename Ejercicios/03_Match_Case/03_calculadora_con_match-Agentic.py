"""
Calculadora mejorada:
    - Solicitar 2 números reales.
    - Solicitar qué operación: +, -, *, /
    - Mostrar resultado

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo3_Match_case
"""

num1 = float(input("Introduce un primer número: "))
num2 = float(input("Introduce un segundo número: "))
operacion = input("Introduce qué operación quieres ejecutar (+, -, *, /): ")

# ==========================================
# 1. FORMA TRADICIONAL (if / elif / else)
# ==========================================
print("\n--- Resultado con IF / ELIF / ELSE ---")

# Esta sección muestra intencionadamente la forma tradicional.
# sourcery skip: switch, assign-if-exp
if operacion == "+":
    resultado = f"{num1} + {num2} = {num1 + num2}"
elif operacion == "-":
    resultado = f"{num1} - {num2} = {num1 - num2}"
elif operacion == "*":
    resultado = f"{num1} * {num2} = {num1 * num2}"
elif operacion == "/":
    if num2 == 0:
        resultado = "Error: No se puede dividir entre 0"
    else:
        resultado = f"{num1} / {num2} = {num1 / num2}"
else:
    resultado = "Operación no válida"

print(resultado)

# ==========================================
# 2. FORMA MODERNA (match / case)
# ==========================================
print("\n--- Resultado con MATCH / CASE ---")

'''
    Estructura match-case (Python 3.10+):
    match variable:
        case valor1:
            codigo
        case valor2:
            codigo
        case _:  # Comodín / Caso por defecto (equivalente a else)
            codigo
'''
# cada caso es una variable:
match operacion:
    case "+":
        resultado_match = f"{num1} + {num2} = {num1 + num2}"
    case "-":
        resultado_match = f"{num1} - {num2} = {num1 - num2}"
    case "*":
        resultado_match = f"{num1} * {num2} = {num1 * num2}"
    case "/":
        if num2 == 0:
            resultado_match = "Error: No se puede dividir entre 0"
        else:
            resultado_match = f"{num1} / {num2} = {num1 / num2}"
    case _:
        resultado_match = "Operación no válida"

print(resultado_match)
