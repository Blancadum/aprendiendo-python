"""
solicitar numeros al usuario hasta que introduzca FIN
    Vamos sumando los números y al final mostrar el resultado

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo6_password
"""

nums = input('Introduzca números a sumar y pare poniendo FIN: ')
inicio = 0

while nums != 'FIN':
    n = int(nums)
    inicio += n
    nums = input('Introduzca números a sumar y pare poniendo FIN: ')

print(inicio)
