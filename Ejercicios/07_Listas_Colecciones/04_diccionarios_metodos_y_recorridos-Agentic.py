"""
Enunciado:
Demostración de Diccionarios (dict) en Python:
- Estructura clave: valor (claves únicas, valores pueden repetirse).
- Métodos keys(), values(), items().
- Acceso seguro con corchetes vs método get().
- Inserción y actualización con asignación directa y método update().
- Eliminación con del, pop() y popitem().
- Ordenación y técnicas de recorrido iterativo (por clave y por tuplas clave-valor).

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 10_Diccionarios
"""

alumnos = {"Juan": 6.4, "Maria": 8.3, "Luis": 6.4, "Adolfo": 7.1}
print("Tipo:", type(alumnos))
print("Diccionario inicial:", alumnos)

# Claves, Valores e Ítems
print("Claves (keys):", alumnos.keys())
print("Valores (values):", alumnos.values())
print("Pares clave-valor (items):", alumnos.items())

# Acceso a elementos
print("\nNota de Luis (con clave directa):", alumnos["Luis"])
print("Nota de Luis (con get()):", alumnos.get("Luis"))
print("Búsqueda de alumno inexistente con get():", alumnos.get("NoExiste"))  # Devuelve None sin error

# Agregar y modificar
alumnos["Pepito"] = 3.5  # Inserción
alumnos["Pepito"] = 5.0  # Modificación
alumnos.update({"Elena": 8.0, "Carlos": 7.5})
print("Tras inserciones y modificaciones:", alumnos)

# Borrar elementos
del alumnos["Adolfo"]
ultimo = alumnos.popitem()
print(f"Tras eliminar 'Adolfo' y el último ({ultimo}):", alumnos)

# Recorrer diccionario
print("\n--- Recorrido iterativo ---")
for nombre, nota in alumnos.items():
    print(f"Alumno: {nombre:<10} | Nota: {nota}")

# Ordenación
print("\nClaves ordenadas:", sorted(alumnos.keys()))
print("Notas ordenadas:", sorted(alumnos.values()))
