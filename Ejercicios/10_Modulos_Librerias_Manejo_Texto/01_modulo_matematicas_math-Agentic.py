"""
Enunciado:
Demostración de utilidades del módulo estándar 'math' de Python:
- Operaciones exponenciales y constantes (math.pow, math.pi).
- Logaritmos y trigonometría (math.log, math.sin, math.radians).
- Factoriales y raíces cuadradas (math.factorial, math.sqrt).
- Redondeos: a decimales fijos (round), al alza (math.ceil) y a la baja (math.floor).

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 12_Modulos
"""

import math

print("Potencia 2 elevado a 8:", math.pow(2, 8))  # 256.0
print("Constante PI:", math.pi)  # 3.141592653589793
print("Logaritmo neperiano de 1000:", math.log(1000))  # 6.907755...
print("Seno de 90 grados:", math.sin(math.radians(90)))  # 1.0
print("Factorial de 4:", math.factorial(4))  # 24
print("Raíz cuadrada de 9:", math.sqrt(9))  # 3.0

# Redondeos
print("\n--- Métodos de Redondeo ---")
print("Redondear a 2 decimales 6.765456:", round(6.765456, 2))  # 6.77
print("Redondear al alza math.ceil(3.89):", math.ceil(3.89))  # 4
print("Redondear al alza math.ceil(3.19):", math.ceil(3.19))  # 4
print("Redondear a la baja math.floor(3.89):", math.floor(3.89))  # 3
print("Redondear a la baja math.floor(3.19):", math.floor(3.19))  # 3
