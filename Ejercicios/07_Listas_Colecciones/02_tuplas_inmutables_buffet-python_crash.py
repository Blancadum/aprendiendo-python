"""
Ejercicio 4-13: Inmutabilidad de tuplas (Buffet)

Enunciado:
Definir un menú fijo de 5 platos en una tupla (estructura inmutable).
Intentar modificar un elemento para comprobar que Python lanza un TypeError, y finalmente
reasignar la tupla completa con una nueva carta de platos.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

foods = ("tallarines", "sopa misho", "arroz 3 delicias", "pollo con almendras", "chop suey")

for food in foods:
    print (food)

foods = ("\ntallarines", "pollo al limón", "arroz 3 delicias", "ternera con salsa de ostras", "chop suey")
for food in foods:
    print(food)
