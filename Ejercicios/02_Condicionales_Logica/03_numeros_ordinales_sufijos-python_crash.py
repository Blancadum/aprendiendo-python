"""
Ejercicio 5-11: Sufijos ordinales con bucle e if-elif-else

Enunciado:
Recorrer los números del 1 al 9 y asignar el sufijo ordinal correcto en inglés (1st, 2nd, 3rd, 4th...) según su terminación.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 5
"""

# This program generates numbers from 1 to 10 and adds their ordinal endings (st, nd, rd, th).

# Initialize an empty list where we will store our numbers.
ordinal_numbers = []

# Use a 'for' loop to iterate through numbers from 1 to 10 (range(1, 11) goes up to, but not including, 11).
for value in range(1, 11):
    # Add the 'number' to our 'ordinal_numbers' list.
    ordinal_numbers.append(value)

# After this loop, 'ordinal_numbers' will contain: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through each 'ordinal' in the 'ordinal_numbers' list.
for ordinal in ordinal_numbers:
    # Use an 'if-elif-else' structure to check the value of each number.
    # If the number is 1, append "st".
    if ordinal == 1:
        print(f"{ordinal}st")
    # If the number is 2, append "nd".
    elif ordinal == 2:
        print(f"{ordinal}nd")
    # If the number is 3, append "rd".
    elif ordinal == 3:
        print(f"{ordinal}rd")
    # For all other numbers (4, 5, 6, 7, 8, 9, 10 in this case), append "th".
    else:
        print(f"{ordinal}th")
