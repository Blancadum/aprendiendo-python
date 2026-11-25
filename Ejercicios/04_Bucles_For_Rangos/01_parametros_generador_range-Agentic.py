"""
Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

# range es un generador de números
# range (inicio, final, salto) el número final no está incluido

#Mostrar los números 0-9
# for numero in range(10): # rango va de 0 hasta número -1
#     print(numero)
#     print(numero, end=" ")
# print() #salto de linea

#Mostrar los números 0-9
# for numero in range(10): # rango va de 0 hasta número -1 --> imprime del 0 al 9
#     print(numero)
#     print(numero, end=" ")
# print() #salto de linea

# Mostrar los números 0-9
# for numero in range(0, 11, 2): # rango va de 0 hasta número -1 --> imprime del 0 al 9
#     print(numero, end=" ")
# print() #salto de linea

# Mostrar los números del 10 al 1 en modo decreciente
# for numero in range (10, 0, -1):
#     print(numero, end=" ")

# Mostrar los números del 10 al 0 en modo decreciente de 2 en 2
for numero in range (10, -1, -2):
    print(numero, end=" ")
