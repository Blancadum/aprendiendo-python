"""
Ejercicio Estadísticas básicas en lista numérica

Enunciado:
Definir una lista de dígitos y calcular su valor mínimo, máximo y la suma acumulada.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 4
"""

digits = [0,1,2,3,4,5,6,7,8,9,10]
print (f"La lista de números es: {digits}")
print (f"El número más pequeño es: {min(digits)}")
print (f"El número más grande es: {max(digits)}")
print (f"La suma es: {sum(digits)}")

digits_remove = digits.pop(0)
print (f"Se va a quitar el número 0 de la lista\ny se van a realizar las mismas operaciones")

print (f"El número más pequeño es: {min(digits)}")
print (f"El número más grande es: {max(digits)}")
print (f"La suma es: {sum(digits)}")

print (f"La lista queda así: {digits}")

print (f"Se ha quitado el número {digits_remove}")
