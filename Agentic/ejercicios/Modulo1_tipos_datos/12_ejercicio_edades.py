'''
    Una piscina permite entrada a los que tienen entre 12 y 65 años
    - comprobar si tiene entre 12 y 65
    - si tiene menos de 12 o más de 65
    - si no tiene 18 años
    - si tiene más de 18 años y menos de 30
'''

edad = 25
'''
    condicion and condicion
    condicion or condicion
    not condicion
'''

edad = int(input("Introduce tu edad: "))

print("¿Tiene más de 12 y menos de 65?: ", edad >= 12 and edad <= 65) #True
print("¿Tiene menos de 12 o más de 65?: ", edad < 12 or edad > 65)  #False
print("¿No tiene 18 años?: ", edad != 18) #True
print("¿Tiene entre 18 y 30 años?: ", edad >= 18 and edad <= 30) #True