"""
Mostrar los números primos del 1 al 100

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

print("Números primos del 1 al 100:")

# 1º bucle: recorre los números a evaluar (del 2 al 100, ya que el 1 no es primo)
for numero in range(2, 101):
    es_primo = all(numero % divisor != 0 for divisor in range(2, numero))

    # Si es primo, lo mostramos
    if es_primo:
        print(numero, end=" ")

print()  # Salto de línea al terminar
