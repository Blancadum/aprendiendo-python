"""
Solicitar una letra al usuario (l, m, x, j, v, s, d)
    decir a qué día de la semana corresponde
    o si no es un día valido

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo3_Match_case
"""

letra = input("Escribe una letra de la semana: (l, m, x, j, v, s, d): ").lower()

match letra:
    case "l":
        print("Lunes")
    case "m":
        print("Martes")
    case "x":
        print("Miércoles")
    case "j":
        print("Jueves")
    case "v":
        print("Viernes")
    case "s":
        print("Sábado")
    case "d":
        print("Domingo")
    case _:
        print("No es un día válido")

# O bien...

letra = input("Escribe una letra de la semana: (l, m, x, j, v, s, d): ")

match letra:
    case "l" | "L":
        print("Lunes")
    case "m" | "M":
        print("Martes")
    case "x" | "X":
        print("Miércoles")
    case "j" | "J":
        print("Jueves")
    case "v" | "V":
        print("Viernes")
    case "s" | "s":
        print("Sábado")
    case "d" | "D":
        print("Domingo")
    case _:
        print("No es un día válido")
