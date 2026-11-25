"""
Ejercicio 5-5: Color de alienígena con if-elif-else

Enunciado:
Cadena if-elif-else para evaluar alien verde (5 pts), amarillo (10 pts) o rojo (15 pts).

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 5
"""

alien_color = "yellow"

if alien_color == "green":
    point = 5
elif alien_color == "yellow":
    point = 10
else:
    point = 15

print (f"Player 1 has earned {point} points!")
