"""
Ejercicio 6-4: Recorrido dinámico de diccionario con items()

Enunciado:
Recorrer de manera automatizada las claves y valores del glosario utilizando un bucle for y el método .items().

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program defines a glossary of Python terms in a dictionary
# and then iterates through the dictionary to print each term and its definition.
# Create a dictionary named 'glossary_words'.
# This dictionary stores common Python keywords/methods as keys (strings)
# and their concise, corrected explanations as values (strings).
# Each key-value pair represents a programming term and its meaning.

glossary_words = {'for' : 'used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects',
                'if' : 'executes a block of code only if a specified condition evaluates to True',
                'else' : 'executes a block of code if the preceding "if" (and any "elif") conditions evaluate to False',
                'print' : 'displays output to the console or other standard output device',
                'something.title()' : 'a string method that returns a new string with the first letter of each word capitalized'
                }

# Use a 'for' loop to iterate through each key-value pair in the 'glossary_words' dictionary.
# The .items() method returns a view of the dictionary's key-value pairs as a list of 2-element tuples.
# 'k' will hold the key (the term), and 'v' will hold the value (its definition) in each iteration.

for k, v in glossary_words.items():
    print (k.title() + " stands for " + v + ".")
