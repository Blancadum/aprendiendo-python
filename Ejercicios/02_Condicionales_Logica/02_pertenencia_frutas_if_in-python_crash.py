"""
Ejercicio 5-7: Comprobación de pertenencia en listas con if in

Enunciado:
Almacenar frutas favoritas en una lista y comprobar de forma independiente mediante
'if fruta in lista' si ciertas frutas están presentes.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 5
"""

fruits = ["kiwi","banana", "watermelon", "apple", "plum"]

favorite_fruits = ["kiwi","watermelon","plum"]

for fruit in fruits:
    if fruit in favorite_fruits:
        print ("You really like " + fruit + "!")
    else:
        print (f"{fruit.title()} not in 'favorite_fruit' list.")
