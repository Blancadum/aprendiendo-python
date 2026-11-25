"""
1. De la lista de datos, mostrar solo las vocales

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

datos = ['t', 'a', 'w', 'p', 'o', 'z', 'i']
vocales = ['a', 'e', 'i', 'o', 'u']

print("--- 1. Solo vocales ---")
for letra in datos:
    if letra.lower() in vocales:
        print(letra)

'''
    2. De la lista de datos, mostrar solo las vocales que están en un índice par
'''
print("\n--- 2. Vocales en índices pares ---")
# Usando range(len(datos)) para tener acceso a la posición (índice)
for i in range(len(datos)):
    if i % 2 == 0 and datos[i].lower() in vocales:
        print(f"Índice {i}: {datos[i]}")
