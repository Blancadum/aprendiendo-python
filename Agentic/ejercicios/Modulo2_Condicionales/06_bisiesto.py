'''
    Solicitar el año (2026, 1996, 2005) y mostrar si es bisiesto o no.
    Es bisiesto si: 
    - si es divisible entre 400
    - o si es divisible entre 4 pero no entre 100
'''
year = int(input("Introduce el año: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")