"""
Ejercicio 5-10: Validación de nombres de usuario únicos (case-insensitive)

Enunciado:
Simular el registro web comprobando si un nuevo nombre de usuario ya está ocupado,
realizando la comparación de forma insensible a mayúsculas y minúsculas (lower()).

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 5
"""

current_users = ["Joey", "roSS", "ChAdler", "rachel", "monica", "Phoebe"]

new_users = ["joey", "Ross", "MONICA", "Homer", "bart"]

current_users_low = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_low:
        print (f"{new_user} not available")
    else:
        print (f"{new_user} available")
