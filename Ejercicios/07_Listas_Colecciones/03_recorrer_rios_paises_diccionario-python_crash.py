"""
Ejercicio 6-5: Ríos y países: recorrido con keys(), values() e items()

Enunciado:
Diccionario con nombres de grandes ríos y países por los que discurren. Iterar sobre las parejas río-país,
solo sobre los ríos con .keys() y solo sobre los países con .values().

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program stores a list of major rivers and the countries they run through in a dictionary.
# It then iterates through the dictionary to print information about each river and its country.
# Create a dictionary named 'rivers_country'.
# This dictionary maps the name of a river (string) as the key to the country (string)
# it runs through as the value.

rivers_country = {'nile' : 'egypt',
                 'amazon' : 'brazil',
                 'yangtse' : 'china'
                }

# Use a 'for' loop to iterate through each key-value pair in the 'rivers_country' dictionary.
# The .items() method returns a view of the dictionary's key-value pairs as a list of 2-element tuples.
# 'river' will hold the key (the river's name), and 'country' will hold the value (the country's name)
# in each iteration.

for river, country in rivers_country.items():

    print (f'\nThe ' + river.title() + ' runs through ' + country.title() + '.')
    print ('River: ' + river.title())
    print ('Country: ' + country.title())
