"""
Ejercicio 4-12: Recorrido independiente de listas clonadas

Enunciado:
Clonar una lista de comidas favoritas, añadir elementos distintos a cada una y recorrerlas
por separado con sendos bucles for.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print ("My favorite food is " + food)

for food in friend_foods:
    print ("My friend's favorite food is " + food)
