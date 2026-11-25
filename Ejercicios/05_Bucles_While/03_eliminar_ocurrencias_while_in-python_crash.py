"""
Ejercicio 7-9: Eliminar todas las ocurrencias de un elemento con while in

Enunciado:
Avisar de que se ha agotado el pastrami y eliminar todas las apariciones de 'pastrami' en la lista
de pedidos utilizando la condición 'while "pastrami" in sandwich_orders:'.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

# Print a message informing the user that pastrami sandwiches are out of stock
print("Sorry, we've run out of pastrami sandwiches, all the pastrami sandwiches will be removed from the order.\n")

# List of sandwich orders, some of which are pastrami (out of stock)
ordered_sandwiches = ['pastrami', 'ham', 'cheese', 'pastrami', 'tuna', 'salami', 'pastrami']

# Empty list to store completed sandwiches
finished_sandwiches = []

# Remove all instances of 'pastrami' from the order list (since it's out of stock)
while 'pastrami' in ordered_sandwiches:
    ordered_sandwiches.remove('pastrami')

# Process the remaining sandwiches in the order they were received
while ordered_sandwiches:
    # Remove the first sandwich from the list and assign it to 'order'
    order = ordered_sandwiches.pop(0)

    # Print confirmation message for each prepared sandwich
    print('I made your ' + order + ' sandwich.')

    # Add the prepared sandwich to the finished list
    finished_sandwiches.append(order)

# After all orders are processed, print a summary of the prepared sandwiches
print('\nThe following sandwiches have been prepared: ')
for sandwich in finished_sandwiches:
    # Print each sandwich with the first letter capitalized
    print('* ' + sandwich.title() + '.')
