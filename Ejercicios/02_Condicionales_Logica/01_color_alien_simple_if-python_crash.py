"""
Ejercicio 5-3: Color de alienígena con if simple

Enunciado:
Simular el puntaje en un videojuego evaluando si el color del alien es 'green'.
Si cumple la condición, otorgar 5 puntos.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 5
"""

alien_color = ("green")

if alien_color != "green":
    point = 10

if alien_color == "green":
    point = 5

print (f"Player 1 has earned {point} points!")
