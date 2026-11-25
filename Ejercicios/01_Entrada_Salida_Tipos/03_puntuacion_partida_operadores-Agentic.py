"""
Crea una variable puntos = 100
    un jugador comienza la partida con 100 puntos, gana 25, pierde 15 y después
    duplica su puntuación.
    Mostrar puntuación final

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo1_tipos_datos
"""

puntos= 100
puntos += 25
puntos -= 15
puntos *= 2

print("Cuántos puntos tiene?", puntos)
print(f"La puntuación final es: {puntos} ")
