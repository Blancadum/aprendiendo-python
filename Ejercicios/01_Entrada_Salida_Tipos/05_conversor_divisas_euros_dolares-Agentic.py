"""
Solicitar importe en euros.
Solicitar a cómo está el cambio a dólares.
Mostrar la conversión: x euros son x dólares.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 1
"""

importe_euros = float(input("Introduzca el importe en euros: "))
cambio_dolares = float(input("Introduzca el cambio a dólares: "))

importe_dolares = importe_euros * cambio_dolares
print(f"{importe_euros} euros son {importe_dolares} dólares")
