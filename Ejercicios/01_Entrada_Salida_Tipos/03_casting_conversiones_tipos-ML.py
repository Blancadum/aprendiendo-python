"""
Actividad: Conversión explícita de tipos de datos (Casting)

Descripción:
Muestra cómo transformar cadenas de texto procedentes de input() a números enteros
con int() y números decimales con float() para operar aritméticamente. Incluye
conversión de números a texto con str() y evaluación numérica de booleanos.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

numero1 = int(input("Introduce un número: "))
print(type(numero1))
numero2 = int(input("Introduce otro número: "))
print(type(numero2))
suma = numero1 + numero2
print("Suma:", suma)

# Convertir un str a número real (float(str))
lado = input("Introduce el lado del cuadrado :") # la parte decimal con .
area_cuadrado = float(lado) * float(lado)
area_cuadrado = float(lado) **2 # Al cuadrado
print("Area del cuadrado: ", area_cuadrado)

# Convertir un int a str. str(int)
# print("Suma:" + suma) # Type error
print("Suma:" + str(suma))

# convertir un booleano a numerico
# False = 0, True = 1
print(8 + False) # 8
print(8 + True) # 9
print(True + False) # 1

# Todos los tipos de dato es convertible a str
print(str(True))
print(str(4.67))
