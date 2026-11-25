"""
Tirar el dado hasta que salga el número 6
    Generar un número aleatorio entre 1 y 6
    Mostrar número generado

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo6_password
"""

import random
lanzamiento = 0
while lanzamiento != 6:
    lanzamiento = random.randint(1, 6)
    print("Resultado:", lanzamiento)
