'''
    Un alumno tiene una nota de 7.5 y pregunta:
    - si la nota es superior a 5
    - si la nota es igual o superior a 7
    - si la nota es inferior a 10
    - si la nota es exactamente 10
    - si la nota es distinta de 5
'''

import math

nota = 7.5
print("La nota es superior a 5?", nota > 5)  # True
print("La nota es mayor o igual a 7?", nota >= 7)  # True
print("La nota es menor a 10", nota < 10)  # True
print(math.isclose(nota, 10))  # False
print(not math.isclose(nota, 5))  # True

