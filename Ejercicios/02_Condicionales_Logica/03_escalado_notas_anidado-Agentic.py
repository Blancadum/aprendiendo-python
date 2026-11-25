"""
Solicitar una nota de 0 a 10 (numero real)
        - Si no está entre 0 y 10, nota no es válida.
        - Si es menor de 5 es suspenso.
        - de 5 a 6, aprobado.
        - de 6 a 7, bien
        - de 7 a 8.5 notable
        - más de 8.6, sobresaliente.
        - 10 exacto, matricula de honor.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo2_Condicionales
"""

nota = float(input("Introduce la nota: "))

if nota == (nota < 0 or nota > 10):
    print("Nota no válida")
elif nota == (nota < 5):
    print("Has suspendido")
elif nota == (5.01 <= nota <= 6):
    print("Has aprobado")
elif nota == (6.01 < nota <= 7):
    print("Bien")
elif nota == (7.01 < nota <= 8.4):
    print("Notable")
if nota == (nota > 8.5):
    print("Sobresaliente")
