"""
Ejercicio 4-10: Segmentación de listas con slices

Enunciado:
A partir de una lista de elementos (meses del año), extraer e imprimir:
1. Los tres primeros elementos ([:3]).
2. Tres elementos intermedios ([3:6]).
3. Los tres últimos elementos ([-3:]).

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

months = ["january","february","march","april","may","june","july","august","september","october","november","december"]

print ("Los primeros tres elementos de la lista son: ")
print (months[0:3])
print ("Los segundos tres elementos de la lista son: ")
print (months[3:6])
print ("Los terceros tres elementos de la lista son: ")
print (months[6:9])
print ("Los últimos tres elementos de la lista son: ")
print (months[9:12])
