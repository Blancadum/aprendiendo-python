"""
Ejercicio 6-9: Anidamiento: diccionario con listas de lugares favoritos

Enunciado:
Crear un diccionario donde las claves son personas y los valores son listas con sus lugares favoritos,
recorriendo las estructuras anidadas.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program stores a list of people and their favorite places using a nested dictionary structure.
# It then iterates through the dictionary to print each person's name and their list of favorite places.

# Create a dictionary named 'fav_places'.
# This dictionary uses people's names (strings) as keys.
# The value associated with each person's name is a 'set' of their favorite places (strings).
# A set is an unordered collection of unique elements, useful here because the order of places doesn't matter
# and duplicate places for one person aren't expected.

fav_places = {
    'marta': {'forks', 'london', 'prague'},
    'jose': {'berlin', 'edinburgh', 'london'},
    'carmela': {'tokyo', 'london', 'bruges'}
}

# Outer loop: Iterate through each key-value pair in the 'fav_places' dictionary.
# The .items() method returns a view of the dictionary's key-value pairs as (key, value) tuples.
# 'name' will hold the person's name (key), and 'places' will hold the set of their favorite places (value).
for name, places in fav_places.items():

    # Print an introductory line indicating whose favorite places are being listed.
    # '\n' adds a new line for better visual separation between different people's entries.
    # name.title() converts the name (e.g., 'marta') to title case ('Marta').
    print(f"\nFavorite places of " + name.title() + " are:")

    # Inner loop: Iterate through each 'place' within the 'places' set for the current person.
    # 'place' will temporarily hold each individual city name from the set.
    for place in places:

        # Print each favorite place, capitalized using .title().
        print(place.title())
