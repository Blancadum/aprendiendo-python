"""
Caso Práctico: Manejo de Excepciones en División de Números

Requerimientos de Ejecución:
1. Solicitar dos números al usuario.
2. Implementar un bloque try-except.
3. Capturar la excepción ValueError (por si introducen caracteres no numéricos).
4. Capturar la excepción ZeroDivisionError (por si dividen entre cero).
5. Mostrar el resultado o un mensaje de error amigable y descriptivo.

Evidencias obligatorias a entregar:
- Archivo .py
- Captura de pantalla provocando un error de división por cero manejado.

Autor: Blanca de Uña Martín
Curso: Python Fundae - Evaluación Módulo 4
"""

try:
    # 1. Solicitar dos números al usuario dentro del bloque try
    numero1 = float(input("Introduce el dividendo: "))
    numero2 = float(input("Introduce el divisor: "))

    # Operación de división
    resultado = numero1 / numero2

# 3. Capturar la excepción si el usuario introduce letras o caracteres no numéricos
except ValueError as error:
    print("Error: Has introducido un valor no numérico.", error)

# 4. Capturar la excepción si se intenta dividir por cero
except ZeroDivisionError as error:
    print("Error: No se puede dividir entre cero.", error)

# 5. Mostrar el resultado cuando la operación se realiza sin errores
else:
    print(f"Resultado de la división: {resultado}")

finally:
    print("Fin de la ejecución.")
