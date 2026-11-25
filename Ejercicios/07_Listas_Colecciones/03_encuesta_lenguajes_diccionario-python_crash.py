"""
Ejercicio 6-6: Comprobación de encuestas con listas y diccionarios

Enunciado:
Comparar una lista de candidatos frente a los que ya han respondido una encuesta en un diccionario,
agradeciendo a los que ya participaron e invitando a los que faltan.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 6
"""

# This program stores information about people's favorite programming languages
# and then processes a 'poll' to check who has taken it.

# Create a dictionary named 'favorite_languages'.
# This dictionary maps a person's name (string key) to a list of their
# favorite programming languages (list of strings as the value).
# This allows for multiple values (languages) to be associated with a single key (person).

favorite_languages = {
      'jen' : ['python', 'rust'],
      'sarah' : ['c'],
      'edward' : ['rust', 'go'],
      'phil' : ['python', 'haskell'],
      'lisa' : ['java', 'c++'],
      'will' : ['rust']
      }

# This tuple contains a list of names of individuals who have already taken the poll.

poll = ('sarah', 'edward', 'lisa', 'will')

# Loop through each key-value pair in the 'favorite_languages' dictionary.
# The .items() method returns a view of the dictionary's key-value pairs.
# 'name' will hold the person's name (key), and 'languages' will hold the list of their favorite languages (value).

for name, languages in favorite_languages.items():
    # Print the person's name, formatted with title case, indicating their favorite languages.
    # '\n' adds a new line for better spacing between entries.
    print(f"\n{name.title()}'s favorite languages are:")

    # Inner loop: Iterate through the list of languages for the current person.
    # 'language' will hold each individual language from the 'languages' list.
    for language in languages:
        # Print each favorite language, indented with a tab ('\t') for clear hierarchy.
        # language.title() formats the language name (e.g., 'python' becomes 'Python').
        print(f"\t{language.title()}")

    # Check if the current person's name is present in the 'poll' tuple.
    # This determines if they have already taken the poll.
    if name in poll:
        # If the person is in the 'poll' tuple, thank them for participating.
        print('Thank you ' + name.title() + ' for taking the poll.')
    else:
        # If the person is NOT in the 'poll' tuple, prompt them to take it.
        print(name.title() + ', you should take the poll!')
