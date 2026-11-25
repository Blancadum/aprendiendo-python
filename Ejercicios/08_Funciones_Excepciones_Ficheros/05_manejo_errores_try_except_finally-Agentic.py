"""
Enunciado:
Demostración de estructura completa try - except - else - finally.
Solicitar dos números al usuario para realizar una división.
Capturar posibles errores:
- ValueError: si el usuario introduce texto en lugar de números.
- ZeroDivisionError: si el usuario introduce 0 como divisor.
- except genérico: para cualquier otro error imprevisto.
- else: muestra el resultado únicamente si no hubo errores.
- finally: bloque que se ejecuta siempre, haya o no ocurrido un error.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 11_Excepciones
"""

# try-except-else-finally

try:
    # Instrucciones susceptibles de provocar un error en tiempo de ejecución
    numero1 = int(input("Introduce dividendo: "))
    numero2 = int(input("Introduce divisor: "))
    division = numero1 / numero2

except ValueError as error:
    print("El valor introducido no es numérico:", error)

except ZeroDivisionError as error:
    print("No se puede dividir por cero:", error)

except Exception as error:
    # Bloque genérico para capturar cualquier otra excepción imprevista
    print("Ha ocurrido un error inesperado:", error)

else:
    # Se ejecuta únicamente si el bloque try finaliza con éxito (sin errores)
    print("Resultado:", division)

finally:
    # Se ejecuta SIEMPRE al final, haya habido o no error
    print("***** FIN *****")
