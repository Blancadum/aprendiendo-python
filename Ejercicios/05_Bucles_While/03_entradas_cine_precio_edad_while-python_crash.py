"""
Ejercicio 7-5: Taquilla de cine con bucle while y tarifas por edad

Enunciado:
Preguntar la edad al espectador en un bucle interactivo y calcular el precio de la entrada:
- Menores de 3 años: gratis.
- Entre 3 y 12 años: 10 $.
- Mayores de 12 años: 15 $.
Finalizar cuando se introduce 'quit'.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 7
"""

print ('Welcome to our fantastic Murcia Kino!')
print ('If you want to leave, please enter "quit".')
active = True

while active:
    age = input('\nPlease, enter your age to know price of the ticket: ')
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print ('The ticket is free!')
        elif age <= 12:
            print ('The ticket costs $10.')
        elif age > 12:
            print ('The ticket costs $15.')
