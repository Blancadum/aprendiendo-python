"""
Solicitar un password al usuario
        menos de 6 caracteres: demasiado corta
        entre 5 y 8 caracteres: débil
        entre 9 y 12 caracteres: aceptable
        más de 12 caracteres: fuerte

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo3_Match_case
"""

password = input("Introduce una contraseña: ")
longitud = len(password)

match longitud:
    case num if num < 6:
        print("demasiado corta")
    case num if (6 <= num <= 8):
        print("débil")
    case num if (9 <= num <= 12):
        print("aceptable")
    case num if num > 12:
        print("fuerte")
    case _:
        print("Contraseña no válida")
