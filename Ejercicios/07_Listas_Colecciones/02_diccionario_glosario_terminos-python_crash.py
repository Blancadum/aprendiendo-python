"""
Ejercicio 6-3: Glosario de términos de Python con diccionario

Enunciado:
Crear un glosario con términos de programación en Python y sus definiciones, mostrándolos de forma estructurada.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program creates a simple glossary of Python terms using a dictionary.
# It then prints each term and its refined definition.

# Create a dictionary named 'glossary_words'.
# This dictionary stores common Python keywords/methods as keys and their
# more precise explanations as values.

glossary_words = {'for' : 'used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects',
                'if' : 'executes a block of code only if a specified condition evaluates to True',
                'else' : 'executes a block of code if the preceding "if" (and any "elif") conditions evaluate to False',
                'print' : 'displays output to the console or other standard output device',
                'something.title()' : 'a string method that returns a new string with the first letter of each word capitalized'
                }
# Print each glossary term and its definition.
# We access each definition by using its corresponding key from the 'glossary_words' dictionary.
# '\n' is used to create a new line, formatting the output for better readability.

print ('* For:\n' + glossary_words['for'] + '.')
print ('* If:\n' + glossary_words['if'] + '.')
print ('* Else:\n' + glossary_words['else'] + '.')
print ('* Print:\n' + glossary_words['print'] + '.')
print ('* Something.title():\n' + glossary_words['something.title()'] + '.')
