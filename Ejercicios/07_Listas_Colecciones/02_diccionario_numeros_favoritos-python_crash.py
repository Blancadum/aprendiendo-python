"""
Ejercicio 6-2: Diccionario de números favoritos

Enunciado:
Almacenar los nombres de varias personas y sus números favoritos en un diccionario clave-valor e imprimirlos.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program stores a list of people and their favorite numbers in a dictionary,
# then prints out each person's favorite number.
favorite_numbers = {
    'Marta' : '13',
    'Jose' : '3',
    'Dani' : '7',
    'Carmela' : '666'
    }

# Access and print Marta's favorite number.
# We retrieve the value associated with the key 'Marta' from the 'favorite_numbers' dictionary.
# The value is then concatenated with a descriptive string.
print ("Marta's favorite number is " + favorite_numbers['Marta'])
# Access and print Jose's favorite number.
print ("Jose's favorite number is " + favorite_numbers['Jose'])
# Access and print Dani's favorite number.
print ("Dani's favorite number is " + favorite_numbers['Dani'])
# Access and print Carmela's favorite number.
print ("Carmela's favorite number is " + favorite_numbers['Carmela'])
