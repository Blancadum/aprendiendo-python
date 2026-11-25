"""
Enunciado:
Guía y catálogo práctico de métodos integrados para manejo y transformación de cadenas de texto (str) en Python:
- upper() y lower(): mayúsculas y minúsculas.
- strip(): eliminación de espacios en blanco en extremos.
- replace(): reemplazo de subcadenas.
- count(): recuento de ocurrencias.
- startswith() y endswith(): comprobación de prefijos y sufijos booleanos.
- split() y join(): división y unión de cadenas.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 13_Manejo_Texto
"""

texto = "   Aprender Python con Fundae es genial y potente   "

print("Texto original:", repr(texto))

# Métodos de formato y limpieza
print("upper():", texto.upper())
print("lower():", texto.lower())
print("strip():", repr(texto.strip()))

# Búsqueda y sustitución
limpio = texto.strip()
print("replace('genial', 'extraordinario'):", limpio.replace("genial", "extraordinario"))
print("count('e'):", limpio.count("e"))

# Comprobaciones de inicio y fin (con 's' de tercera persona)
print("startswith('Aprender'):", limpio.startswith("Aprender"))
print("endswith('potente'):", limpio.endswith("potente"))

# División y unión
palabras = limpio.split(" ")
print("split(' '):", palabras)
unido = " - ".join(palabras)
print("join(' - '):", unido)
