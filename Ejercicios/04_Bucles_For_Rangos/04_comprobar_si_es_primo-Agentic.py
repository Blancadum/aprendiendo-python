"""
Solicitar al usuario un número entero
    mostrar si es primo o no
    un número primo es primo si solo es divisible por si mismo y la unidad
    crear un bucle para buscar sus posibles divisores: 2 hasta número -1

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

numero = int(input("Introduce un número entero: "))

# Los números menores o iguales a 1 no son primos
if numero <= 1:
    print(f"El número {numero} no es primo.")
else:
    es_primo = all(numero % divisor != 0 for divisor in range(2, numero))

    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
