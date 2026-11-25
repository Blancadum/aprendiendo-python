"""
Ejercicio 7-8: Procesamiento de pedidos de sándwiches con while y pop

Enunciado:
Lista de pedidos de sándwiches pendientes. Procesar cada uno extrayéndolo con pop() mientras la lista tenga elementos,
trasladándolo a una lista de sándwiches terminados.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

# Initial list of sandwiches to be made
ordered_sandwiches = ['pastrami', 'ham', 'cheese', 'tuna', 'salami']

# Empty list to hold completed sandwiches
finished_sandwiches = []

# Process each sandwich in the order they appear
while ordered_sandwiches:
    # Remove the first sandwich from the list
    order = ordered_sandwiches.pop(0)

    # Print confirmation that the sandwich is made
    print('I made your ' + order + ' sandwich.')

    # Add the prepared sandwich to the finished list
    finished_sandwiches.append(order)

# Display the list of all sandwiches that were prepared
print('\nThe following sandwiches have been prepared: ')
for sandwich in finished_sandwiches:
    # Capitalize the first letter of each sandwich type
    print('* ' + sandwich.title() + '.')
