"""
Ejercicio 5-6: Clasificación de etapas de la vida por edad

Enunciado:
Determinar la etapa vital de una persona según su edad (bebé < 2, infante 2-4, niño 4-13,
adolescente 13-20, adulto 20-65, anciano >= 65) usando if-elif-else.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 5
"""

age = 80

if age < 2:
    print ("It's a baby")
elif age == 2 or age < 4:
    print ("It's a toddler")
elif age == 4 or age < 13:
    print ("It's a kid")
elif age == 13 or age < 20:
    print ("It's a teenager")
elif age == 20 or age < 65:
    print ("It's an adult")
elif age >= 65:
    print ("It's an elder")
