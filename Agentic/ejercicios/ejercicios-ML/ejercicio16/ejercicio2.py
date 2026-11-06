"""
Blanca de Uña Martín
"""

# Importación de la libreria para usar comandos del sistema
import os

# Limpiar la pantalla de la terminal (cls para Windows, clear para Mac/Linux)
os.system("clear")

#I. Escribe un programa que pregunte al usuario los dos lados de un rectángulo y presente por pantalla el cálculo del perímetro (suma de los lados) y el área (base por altura) redondeando a dos decimales.
lado1 = float(input("Introduce el primer lado del rectángulo: "))
lado2 = float(input("Introduce el segundo lado del rectángulo: "))

perimetro = 2 * (lado1 + lado2)
area = lado1 * lado2

print(f"Perímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")