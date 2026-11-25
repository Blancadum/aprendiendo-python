"""
Ejercicio Lista acumulada de cuadrados con append

Enunciado:
Generar una lista vacía y agregar progresivamente los cuadrados de los números del 1 al 10 mediante append().

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print (squares)
