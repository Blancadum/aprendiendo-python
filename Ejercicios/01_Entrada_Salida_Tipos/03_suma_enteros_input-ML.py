"""
Actividad: Lectura por teclado, conversión de tipos y concatenación

Descripción:
Captura dos números introducidos como cadenas de texto mediante input(),
los convierte a enteros con int(), realiza la suma y muestra el resultado
concatenándolo mediante str().

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

num1 = input("Introduce un número: ")
num1 = int(num1)

num2 = input("Introduce otro número: ")
num2 = int(num2)

suma = num1 + num2

print("La suma de los numeros es: " + str(suma))
