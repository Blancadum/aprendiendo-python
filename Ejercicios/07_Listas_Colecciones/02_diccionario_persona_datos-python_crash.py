"""
Ejercicio 6-1: Diccionario con datos de persona

Enunciado:
Almacenar el nombre, apellido, edad y ciudad de una persona en un diccionario e imprimir cada dato.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program stores information about a person in a dictionary

"""
Create a dictionary named 'person'.
Dictionaries store data in 'key-value' pairs.
Each key (like 'first name', 'last name', etc.) is unique and used to access its associated value.
"""
person = {'first_name' : 'Marta', 'last_name' : 'SC', 'age' : '33', 'city' : 'Montcada i Reixac'}

# Print an introductory message.
print("Today we introduce Marta")

# Access the dictionary values using their keys and concatenate them with text.
# Use person['first name'] to get the value associated with the 'first name' key.
print("Her first name is " + person['first_name'])

# Access the last name in the same way.
print("Her last name is " + person['last_name'])

# Access the age.
print("Her age is " + person['age'] + " years old")

# Finally, access the city.
print("The city where she lives is " + person['city'])
