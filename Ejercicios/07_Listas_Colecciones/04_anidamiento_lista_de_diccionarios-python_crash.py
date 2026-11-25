"""
Ejercicio 6-7: Anidamiento: lista de diccionarios de personas

Enunciado:
Crear varios diccionarios con datos de diferentes personas y agruparlos en una lista, recorriéndola para imprimir cada ficha.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program defines information for multiple people using dictionaries,
# stores these dictionaries in a list, and then iterates through the list
# to print details about each person.

# Create a dictionary named 'person_1' to store details for the first person.
# Keys represent attributes (e.g., 'first_name', 'last_name') and values are the corresponding data.

person_1 = {'first_name': 'Marta', 'last_name': 'SC', 'age': '33', 'city': 'Montcada i Reixac'}

# Create a dictionary named 'person_2' for the second person.

person_2 = {'first_name': 'Carmela', 'last_name': 'MM', 'age': '31', 'city': 'Alcantarilla'}

# Create a dictionary named 'person_3' for the third person.

person_3 = {'first_name': 'Dani', 'last_name': 'GC', 'age': '32', 'city': 'Stockholm'}

# Create a list named 'people'.
# This list will hold all the individual person dictionaries, making it easy to manage
# and iterate over multiple person records.

people = [person_1, person_2, person_3]

# Loop through each dictionary (representing a 'person') in the 'people' list.
# In each iteration, the variable 'person' will temporarily hold one of the dictionaries (person_1, then person_2, etc.).

for person in people:

    # Print an introductory message for the current person.
    # We access the 'first_name' value from the current 'person' dictionary.
    print("\nLet's introduce " + person['first_name'] + ".")

    # Print the last name, accessing the 'last_name' value.
    print("His/her last name is: " + person['last_name'] + ".")

    # Print the age, accessing the 'age' value.
    # The 'age' is stored as a string, allowing direct concatenation.
    print("He/She is " + person['age'] + " years old.")

    # Print the city, accessing the 'city' value.
    print("He/She lives in the city of " + person['city'] + ".")
