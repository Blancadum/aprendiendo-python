"""
Actividad: Suma de dos números leídos por teclado

Descripción:
Captura dos valores mediante input(), los convierte a números enteros con int(),
calcula su suma y muestra el resultado en consola concatenando con str().

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

num1 = input("Introduce un número: ")
num1 = int(num1)

num2 = input("Introduce otro número: ")
num2 = int(num2)

suma = num1 + num2

print("La suma de los numeros es: " + str(suma))
