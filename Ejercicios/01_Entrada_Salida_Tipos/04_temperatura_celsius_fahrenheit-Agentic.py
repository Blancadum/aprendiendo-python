"""
Conversión de grados centígrados a Fahrenheit
    Solicitar la temperatura en grados centígrados (float)
    aplicar la fórmula para obtener los grados Fahrenheit

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo1_tipos_datos
"""

celsius = float(input("Introduce la temperatura en grados centígrados: "))
fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")
