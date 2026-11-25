"""
Ejercicio 4-1: Recorrido de pizzas con bucle for

Enunciado:
Almacenar tipos de pizzas favoritas en una lista y utilizar un bucle for para imprimir
una frase sobre cada una de ellas, finalizando con un mensaje general.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

pizzas = ["margheritta" , "calzone" , "4 formaggi"]

for pizza in pizzas:
    print ("Me encanta la pizza " + pizza.title())

print ("¡Guau, me encanta la pizza!")
