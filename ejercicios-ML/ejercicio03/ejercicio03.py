"""
Blanca de Uña Martín
"""

TASA_CAMBIO = 1.33250

dolares = float(input("Introduce la cantidad de dólares: "))
euros = dolares / TASA_CAMBIO
print(f"El cambio es {round(euros, 2)} euros.")

euros_usuario = float(input("Introduce la cantidad de euros: "))
dolares_usuario = euros_usuario * TASA_CAMBIO
print(f"El cambio es {round(dolares_usuario, 2)} dólares.")
