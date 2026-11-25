"""
Enunciado:
Dada una lista con elementos tipo texto ('1', 'dos', '3', '4', '5'), se pretende
convertir cada elemento a tipo int y acumular su suma.
Al recorrer la lista por índice, se fuerza un rango extendido range(len(datos) + 1)
para provocar y capturar:
1. IndexError: al intentar acceder a datos[5] (fuera de rango).
2. ValueError: al intentar convertir 'dos' a número entero.
3. Except genérico: para cualquier otra eventualidad.
4. Else: acumular el número únicamente si la conversión y el acceso tuvieron éxito.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 11_Excepciones
"""

datos = ["1", "dos", "3", "4", "5"]
suma = 0

# range(len(datos) + 1) genera índices de 0 a 5, forzando un IndexError al final
for idx in range(len(datos) + 1):
    try:
        # 1. Acceder al elemento por su índice
        dato = datos[idx]

        # 2. Convertir texto a número entero
        numero = int(dato)

    except IndexError as error:
        print("Índice fuera de rango:", error)

    except ValueError as error:
        print("El valor no es numérico:", error)

    except Exception as error:
        print("Ha ocurrido un error inesperado:", error)

    else:
        # Solo se acumula si no se ha producido ninguna excepción en el bloque try
        suma += numero

print("\nSuma total:", suma)
