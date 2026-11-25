"""
Ejercicio 7-4: Selección de ingredientes de pizza con while y centinela

Enunciado:
Bucle interactivo while que solicita ingredientes para pizza hasta que el usuario introduce 'quit',
confirmando cada ingrediente añadido.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

# This program simulates a pizza topping selection process.
# Users can choose toppings, view their current selections, or quit.

# --- Topping Definitions & Initialization ---

# Tuple of available pizza toppings (tuple).
pizza_toppings = ('mozzarella', 'mushrooms', 'bacon', 'olives', 'pepperoni', 'cheddar', 'tomato', 'onion', 'garlic')

# List to store toppings selected by the user.
pizza_topping = []

# Control variable for the main selection loop.
active = True

# --- Display Available Toppings ---
print ('Welcome to our italian pizzeria!')
print('The available toppings are:')
# Loop and print each available topping.
for pizzas in pizza_toppings:
    print('* ' + pizzas.title() + '.')

# Inform the user how to exit the program.
print ("\nIf you want to quit the program, just enter 'quit' at any moment.")
# Inform the user how to view their current toppings.
print ("If you want to see a list of the toppings you've just added to your pizza, type 'list'")

# --- Main Topping Selection Loop ---

# Loop continues until 'active' is False.
while active:
    # Get user input and convert to lowercase.
    requested_topping = input('\nWhat pizza topping would you like to add to your pizza? ').lower()

    # Check if user wants to quit.
    if requested_topping == 'quit':
        active = False # Exit loop
    # Process user input.
    else:
        # Check if requested topping is available.
        if requested_topping in pizza_toppings:
            print(f'Adding {requested_topping} to your pizza!')
            pizza_topping.append(requested_topping) # Add to user's pizza
        # Check if user wants to list current toppings.
        elif requested_topping == 'list':
            print('\nYour pizza has the following toppings:\n')
            # Loop and print each selected topping. Remove duplicate items too.
            for topping in set(pizza_topping):
                print('* ' + topping.title())
        # If topping is not available.
        elif requested_topping not in pizza_toppings:
            print('That topping is not available.')
