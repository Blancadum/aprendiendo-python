"""
Ejercicio 6-8: Anidamiento: lista de diccionarios de mascotas

Enunciado:
Crear varios diccionarios para distintas mascotas (tipo de animal y nombre del dueño),
almacenarlos en una lista e iterar para mostrar sus datos.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program defines information for multiple pets using dictionaries,
# stores these dictionaries in a list, and then iterates through the list
# to print specific details for each pet.

# Create several dictionaries (pet_1 through pet_9), where each dictionary
# represents a single pet. Each dictionary stores attributes like 'name',
# 'owner', and 'species' as key-value pairs.

pet_1 = {'name': 'bora', 'owner': 'mum', 'species': 'hamster'}
pet_2 = {'name': 'mochi', 'owner': 'carmela', 'species': 'hamster'}
pet_3 = {'name': 'gamora', 'owner': 'me', 'species': 'cat'}
pet_4 = {'name': 'nebula', 'owner': 'me', 'species': 'cat'}
pet_5 = {'name': 'indie', 'owner': 'me', 'species': 'cat'}
pet_6 = {'name': 'ton', 'owner': 'mum', 'species': 'bird'}
pet_7 = {'name': 'habichuela', 'owner': 'alvaro', 'species': 'cat'}
pet_8 = {'name': 'tula', 'owner': 'marta', 'species': 'dog'}
pet_9 = {'name': 'flu', 'owner': 'marta', 'species': 'fish'}

# Create a list named 'pets'.
# This list aggregates all the individual pet dictionaries, allowing for
# easy management and iteration over the entire collection of pets.

pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6, pet_7, pet_8, pet_9]

# Outer loop: Iterate through each dictionary (representing a 'pet') in the 'pets' list.
# In each iteration, 'pet' will hold one of the pet dictionaries.

for pet in pets:

    # Inner loop: Iterate through each key-value pair within the current 'pet' dictionary.
    # The .items() method returns key-value pairs as (key, value) tuples.
    # 'k' will hold the key (e.g., 'name', 'owner', 'species'), and 'v' will hold the value.
    for k, v in pet.items():

        # If the key is 'name', print 'Name:' followed by the capitalized value.
        # '\n' adds a new line before the 'Name:' output for visual separation of pet details.
        if k == 'name':
            print(f"\nName: " + v.title() + ".")

        # If the key is 'owner', print 'Owner:' followed by the capitalized value.
        elif k == 'owner':
            print('Owner: ' + v.title() + ".")

        # For any other key (in this case, only 'species'), print 'Species:'
        # followed by the capitalized value.
        else:  # This 'else' specifically catches the 'species' key
            print('Species: ' + v.title() + ".")
