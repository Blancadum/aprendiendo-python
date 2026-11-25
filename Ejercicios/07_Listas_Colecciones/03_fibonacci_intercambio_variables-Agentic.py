"""
OJO!!! no hasta el numero 100

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo5_Fibbonacci
"""

termino1 = 0
termino2 = 1
print(termino1, termino2, sep=", ", end=", ")
for num in range(1, 9):
    termino3 = termino1 + termino2
    print(termino3, end=", ")
    # cambiar posiciones
    termino1 = termino2
    termino2 = termino3
