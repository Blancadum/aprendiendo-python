"""
Solicitar el password al usuario hasta que aceierte que es "curso"

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo6_password
"""

pw = ""
while pw != "curso":
    pw = input("Introduce la contraseña: ")
    print("Password correcta")
