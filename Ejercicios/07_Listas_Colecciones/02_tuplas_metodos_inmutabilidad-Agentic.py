"""
Enunciado:
Demostración de Tuplas en Python:
- Propiedades: colecciones ordenadas (con índice), inmutables y permiten duplicados.
- Sintaxis con paréntesis y tupla de un solo elemento (coma final obligatoria).
- Métodos count() e index().
- Concatenación de tuplas y conversiones entre lista y tupla.
- Slices y funciones universales (len, min, max, sum, sorted).

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 8_Tuplas
"""

# Las tuplas son inmutables: no podemos agregar, eliminar ni modificar sus datos
dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
print("Tipo:", type(dias))
print("Contenido:", dias)

# Acceso por índice y propiedades
print("Primer día:", dias[0])
print("Longitud de la tupla:", len(dias))
print("Veces que aparece 'lunes':", dias.count("lunes"))
print("Posición de 'viernes':", dias.index("viernes"))

# Concatenación: para una tupla de un solo elemento es obligatoria la coma final
otra_tupla = dias + ("otro_sabado",)
print("Tupla ampliada:", otra_tupla)

# Conversión entre lista y tupla
lista_dias = list(otra_tupla)
lista_dias.append("dia_extra")
tupla_reconertida = tuple(lista_dias)
print("Reconvertida a tupla:", tupla_reconertida)

# Slicing
print("Días laborables [0:5]:", dias[0:5])
print("Días en orden inverso [::-1]:", dias[::-1])

# Funciones universales sobre tuplas numéricas
numeros = (1, 2, 3, 4, 5)
print("\n--- Funciones Universales ---")
print("Longitud:", len(numeros))
print("Mínimo:", min(numeros))
print("Máximo:", max(numeros))
print("Suma:", sum(numeros))
print("Orden descendente:", sorted(numeros, reverse=True))
print("Duplicación por repetición (* 2):", numeros * 2)
