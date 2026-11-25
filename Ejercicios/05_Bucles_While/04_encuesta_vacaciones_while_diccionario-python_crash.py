"""
Ejercicio 7-10: Encuesta de vacaciones soñadas con while y diccionario

Enunciado:
Realizar una encuesta a varios usuarios sobre el destino de sus vacaciones soñadas,
almacenando las respuestas en un diccionario y mostrando el resumen final.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

# This program conducts a simple poll to find out users' dream vacation destinations.
# It asks a specified number of users for their input and then displays the results.

# Inform users about the poll's purpose.
print("\nLet's take a poll to ask users where they would go on vacation")

# Get the number of users who will participate in the poll.
# Convert the input (string) to an integer.
users = int(input('How many users will take the poll? '))

count = 0 # Initialize a counter for the loop.
fav_places = [] # Initialize an empty list to store favorite places.

# Loop until the 'count' reaches the specified 'users' number.
while count < users:
    # Prompt user for their dream vacation place and add it to the 'fav_places' list.
    fav_places.append(input('If you could visit one place in the world, where would you go? '))
    count += 1 # Increment the counter for each user polled.

print('\nThe results of the poll are: ') # Inform user that results are being displayed.
# Loop through each place in the 'fav_places' list.
for place in fav_places:
    # Print each submitted place, formatted with an asterisk.
    print(f'* {place}')
