"""
Ejercicio 4-5: Suma y extremos de un millón de números (min, max, sum)

Enunciado:
Crear una lista del 1 al 1.000.000 y comprobar sus valores mínimo (min), máximo (max)
y la sumatoria total mediante la función sum().

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

numeros = list(range(1,1000001))
print (min(numeros))
print (max(numeros))
print (sum(numeros))
