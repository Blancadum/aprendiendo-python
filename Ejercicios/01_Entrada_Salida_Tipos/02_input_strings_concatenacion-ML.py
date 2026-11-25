"""
Actividad: Entrada de datos por consola con input() y concatenación

Descripción:
Demuestra el comportamiento de la función input() al capturar datos del usuario,
evidenciando que toda entrada se interpreta inicialmente como cadena de texto (str)
y que el operador '+' concatena en lugar de sumar cuando no se realiza conversión.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

numero1 = input("Introduce un número: ")
print(type(numero1))
numero2 = input("Introduce otro número: ")
print(type(numero2))
suma = numero1 + numero2
print("Suma:", suma)
