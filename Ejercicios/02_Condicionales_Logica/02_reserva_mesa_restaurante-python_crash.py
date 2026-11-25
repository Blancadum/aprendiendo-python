"""
Ejercicio 7-2: Comprobación de reserva en restaurante

Enunciado:
Preguntar cuántas personas son en el grupo. Si son más de 8, informar de que deberán esperar una mesa;
en caso contrario, indicar que su mesa está lista.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

dinner_group = input ('How many people are in your dinner group? ')
dinner_group = int(dinner_group)
if dinner_group > 8:
    print ("You'll have to wait for a table.")
else:
    print ('Your table is ready!')
