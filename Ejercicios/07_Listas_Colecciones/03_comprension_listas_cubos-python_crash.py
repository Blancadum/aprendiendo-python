"""
Ejercicio 4-9: Comprensión de listas para cubos

Enunciado:
Generar la lista de los primeros 10 cubos de forma compacta mediante una comprensión de listas (list comprehension).

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

cubes = [value**3 for value in range(1,11)]
print (cubes)
