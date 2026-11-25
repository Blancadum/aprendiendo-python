"""
Enunciado:
Operaciones algebraicas y relacionales avanzadas entre conjuntos (set) en Python:
1. Intersección (& / intersection): elementos comunes.
2. Diferencia (- / difference): elementos del primer conjunto que no están en el segundo.
3. Unión (| / union): todos los elementos sin duplicados.
4. Diferencia simétrica (^ / symmetric_difference): elementos que están en uno u otro pero no en ambos.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 9_Conjuntos
"""

numeros1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros2 = {0, 2, 4, 6, 8, 10}

print("Conjunto 1:", numeros1)
print("Conjunto 2:", numeros2)

# Intersección: elementos comunes
print("\n--- Intersección (&) ---")
print("Método intersection():", numeros1.intersection(numeros2))
print("Operador &:", numeros1 & numeros2)

# Diferencia: elementos en numeros1 que no están en numeros2
print("\n--- Diferencia (-) ---")
print("numeros1 - numeros2:", numeros1 - numeros2)
print("numeros2 - numeros1:", numeros2 - numeros1)

# Unión: todos los elementos
print("\n--- Unión (|) ---")
print("Método union():", numeros1.union(numeros2))
print("Operador |:", numeros1 | numeros2)

# Diferencia simétrica: la unión menos los comunes
print("\n--- Diferencia Simétrica (^) ---")
print("Método symmetric_difference():", numeros1.symmetric_difference(numeros2))
print("Operador ^:", numeros1 ^ numeros2)
