"""
Enunciado:
Demostración exhaustiva de creación, manipulación y métodos fundamentales de listas en Python:
- Creación de listas heterogéneas y listas vacías.
- Concatenación de listas y cálculo de longitud con len().
- Acceso a elementos con indexación positiva y negativa.
- Inserción y adición con append(), insert() y extend().
- Modificación y eliminación de elementos con remove().
- Búsqueda y conteo con index() y count().
- Recorrido iterativo con for in y for range.
- Explicación didáctica de la cláusula 'else' en bucles for vs 'break'.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 7_Listas
"""

# Lista: colecciones ordenadas de elementos (tienen índice)
# Permite elementos duplicados, de diferentes tipos y son mutables (añadir, modificar, eliminar)
list1 = ["Maria", "Pérez", 30, "soltera", "sin hijos"]
list2 = ["estudiante", "medicina", "20020"]

# Tipo de listas
print(type(list1))  # <class 'list'>

# Mostrar las listas
print("Lista 1:", list1)
print("Lista 2:", list2)

# Crear lista vacía
lista_vacia = []
lista = list()

# Unir listas (el orden es relevante)
lista_vacia = list1 + list2
print("Lista unida (list1 + list2):", lista_vacia)
lista = list2 + list1
print("Lista unida (list2 + list1):", lista)

# Longitud de la lista (número de elementos)
print("Longitud de la lista:", len(lista))

# Acceso a elementos de la lista
# Índice positivo: desde la izquierda (comienza en 0)
# Índice negativo: desde la derecha (comienza en -1)
print("Código postal:", lista[2])
print("Estado civil (negativo):", lista[-2])
print("Último elemento:", lista[len(lista) - 1])

# Agregar un elemento al final de la lista
lista.append("morena")
print("Tras append:", lista)

# Agregar elemento en una posición determinada
lista.insert(0, 1.75)
print("Tras insert(0, 1.75):", lista)

# Agregar varios elementos a la vez al final
lista.extend([1, 2, 3])
print("Tras extend([1, 2, 3]):", lista)

# Eliminar un elemento por su valor
list1.remove("Maria")
print("list1 tras remove('Maria'):", list1)

# Modificar un elemento de la lista
lista[-4] = "1 hijo"
print("Tras modificación:", lista)

# Mostrar el índice donde está un elemento
print("Medicina está en el índice:", lista.index("medicina"))

# Contar cuántos elementos coinciden con el valor
print("Elementos 'estudiante':", lista.count("estudiante"))

# Recorrer la lista con for in y cláusula else
print("\nRecorrido con for in:")
for elemento in lista:
    print(elemento, end=" - ")
else:
    print("\nFin del recorrido (sin interrupción por break).")

# Recorrer la lista por índice con for range
print("\nRecorrido con for range:")
for indice in range(len(lista)):
    print(f"Índice {indice}: {lista[indice]}")
