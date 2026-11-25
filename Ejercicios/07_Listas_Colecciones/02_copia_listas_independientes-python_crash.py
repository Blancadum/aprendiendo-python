"""
Ejercicio 4-11: Copia independiente de listas con slice [:]

Enunciado:
Demostrar cómo clonar una lista utilizando el operador de corte [:] para que las modificaciones
en una lista no afecten a la otra, comprobando su independencia.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

my_pizzas = ["margheritta" , "calzone" , "4 formaggi"]
your_pizzas = my_pizzas[:]

my_pizzas.append("diavola")
your_pizzas.append("barbacoa")

for pizza in my_pizzas:
    print ("Me encanta la pizza " + pizza.title())

for pizza in your_pizzas:
    print ("A mis amigos les encanta la pizza " + pizza.title())

print (my_pizzas)
print (your_pizzas)
