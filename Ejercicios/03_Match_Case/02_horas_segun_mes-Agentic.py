"""
solicitar al usuario un número del 1 al 12
    calcular cuantas horas tiene el mes

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo3_Match_case
"""

mes = input ("Introduce un número del mes (1-12): ")

match mes:
    # Meses con 31 días (744 horas)
    case "1" | "3" | "5" | "7" | "8" | "10" | "12":
        dias = 31
        horas = dias * 24
        print (f"El mes {mes} tiene {dias} días, lo que equivale a {horas} horas.")

    # Meses con 30 días (720 horas)
    case "4" | "6" | "9" | "11":
        dias = 30
        horas = dias * 24
        print (f"El mes {mes} tiene {dias} días, lo que equivale a {horas} horas.")

    # Febrero (28 o 29 días)
    case "2":
        print ("El mes 2 (febrero) tiene 28 (672 horas), o 29 (696 horas) si es bisi días.")

    case _:
        print("Error: Debes introducir un número válido del 1 al 12.")
