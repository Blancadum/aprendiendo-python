"""
Enunciado:
Ejercicio integral de análisis y manipulación de texto sobre la frase:
frase = "Me gusta Java porque Java es divertido"

Operaciones requeridas:
1. Sustituir 'Java' por 'Python'.
2. Contar cuántas veces aparece la palabra 'Java'.
3. Comprobar si empieza por "Me gusta".
4. Comprobar si termina por "divertido".
5. Calcular su longitud con len().
6. Obtener el carácter máximo y mínimo con max() y min().
7. Transformar la frase a mayúsculas con upper().
8. Transformar la frase a minúsculas con lower().

Incluye notas didácticas sobre errores frecuentes de sintaxis en Python.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 13_Manejo_Texto
"""

# Declaración de la variable al inicio (orden secuencial de ejecución)
frase = "Me gusta Java porque Java es divertido"

# 1. Sustituir Java por Python
frase1 = frase.replace("Java", "Python")
print("1. Sustituir Java por Python:", frase1)

# 2. Cuántas veces aparece la palabra Java
frase2 = frase.count("Java")
print("2. Cuántas veces aparece 'Java':", frase2)

# 3. Comprobar si empieza por "Me gusta"
frase3 = frase.startswith("Me gusta")
print("3. Comprobar si empieza por 'Me gusta':", frase3)

# 4. Comprobar si termina por "divertido"
frase4 = frase.endswith("divertido")
print("4. Comprobar si termina por 'divertido':", frase4)

# 5. Longitud total
frase5 = len(frase)
print("5. Longitud de la frase:", frase5)

# 6. Carácter máximo y mínimo (funciones universales)
frase6_max = max(frase)
frase6_min = min(frase)
print("6. Carácter máximo (código ASCII):", frase6_max)
print("6. Carácter mínimo (código ASCII):", repr(frase6_min), "(espacio en blanco)")

# 7. Transformar a Mayúsculas
frase7 = frase.upper()
print("7. Transformar a mayúsculas:", frase7)

# 8. Transformar a minúsculas
frase8 = frase.lower()
print("8. Transformar a minúsculas:", frase8)

# ==============================================================================
# 📝 APUNTES DIDÁCTICOS: RESUMEN DE REGLAS CLAVE
# ==============================================================================
# 1. ORDEN SECUENCIAL: Declarar variables antes de invocarlas o leerlas.
# 2. PREFIJOS/SUFIJOS: .startswith() y .endswith() llevan 's' al final.
# 3. MÉTODOS vs FUNCIONES BUILT-IN:
#    - Métodos específicos de string: frase.upper(), frase.replace(), frase.count().
#    - Funciones globales universales: len(frase), max(frase), min(frase).
# ==============================================================================
