"""
Ejercicio 6-10: Anidamiento: múltiples números favoritos por persona

Enunciado:
Modificar el diccionario de números favoritos para que cada persona tenga asociada una lista de varios números favoritos.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program stores a list of people and their multiple favorite numbers in a nested dictionary.
# It then iterates through this structure to print out each person's name and their list of favorite numbers.

# Create a dictionary named 'favorite_numbers'.
# This dictionary uses people's names (strings) as keys.
# The value associated with each person's name is another dictionary.
# This inner dictionary stores multiple favorite numbers, with keys like 'number_1', 'number_2', etc.,
# and their corresponding number values (stored as strings).
# We could optimized this program if we use a list inside the favorite_numbers dictionary
# instead of nested dictionaries. But the purpouse of this exercise is using nested dictionaries.

favorite_numbers = {
    'Marta' : {'number_1' : '13',
               'number_2' : '7',
               'number_3' : '30'
               },
    'Jose' : {'number_1' : '3',
              'number_2' : '33',
              'number_3' : '42'
              },
    'Dani' : {'number_1' : '7',
              'number_2' : '1',
              'number_3' : '10'
              },
    'Carmela' : {'number_1' : '666',
                 'number_2' : '16',
                 'number_3' : '17'
                 }
    }

# Outer loop: Iterate through each key-value pair in the 'favorite_numbers' dictionary.
# The .items() method returns a view of the dictionary's key-value pairs as (key, value) tuples.
# 'user' will hold the person's name (outer dictionary key).
# 'fav_numbers' will hold the inner dictionary containing that person's specific favorite numbers.

for user, fav_numbers in favorite_numbers.items():

    # Print an introductory line, indicating whose favorite numbers are being listed.
    # '\n' adds a new line for better visual separation between different people's entries.
    # We use an f-string for clear formatting, embedding the 'user' variable directly.

    print(f"\n{user}'s favorite numbers are: ")

    # Inner loop: Iterate through each key-value pair within the 'fav_numbers' (inner) dictionary.
    # 'number' will hold the key (e.g., 'number_1', 'number_2').
    # 'fav_number' will hold the value (the actual favorite number, e.g., '13', '7').

    for number, fav_number in fav_numbers.items():

        # Print the actual favorite number.
        # Note: The 'number' variable (the inner dictionary key like 'number_1') is not used in the print statement,
        # only the 'fav_number' (the value like '13').

        print(fav_number)
