"""
Ejercicio 7-3: Comprobación de múltiplos de diez con módulo %

Enunciado:
Solicitar un número entero y determinar si es múltiplo de 10 evaluando si 'numero % 10 == 0'.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

number = input ("Enter a number and I'll tell you if that number is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print ('That number is a multiple of 10.')
else:
    print ('That number is not a multiple of 10.')
