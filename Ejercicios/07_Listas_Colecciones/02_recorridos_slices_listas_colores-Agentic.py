"""
Enunciado:
Demostración práctica de listas, técnicas de recorrido y operaciones avanzadas de slicing:
1. Crear una lista 'colores' con ['rojo', 'verde', 'azul'].
2. Recorrer la lista con for-in, for-range y while.
3. Métodos append, insert y remove.
4. Unir listas y extraer rodajas (slices) completas:
   - Primeros y últimos elementos.
   - Rangos intermedios y con saltos (step).
   - Inversión completa de listas con paso negativo [::-1].

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 7_Listas
"""

colores = ["rojo", "verde", "azul"]

print("Tipo de colección:", type(colores))
print("Contenido inicial:", colores)

# Recorrer la lista con for in
print("\n--- Recorrer con for in ---")
for color in colores:
    print(color)

# Recorrer la lista con for range
print("\n--- Recorrer con for range ---")
for i in range(len(colores)):
    print(f"[{i}]: {colores[i]}")

# Recorrer la lista con while
print("\n--- Recorrer con while ---")
i = 0
while i < len(colores):
    print(f"[{i}]: {colores[i]}")
    i += 1

# Acceso y modificación
print("\nColor verde por índice [1]:", colores[1])
colores.remove("azul")
print("Lista tras borrar azul:", colores)

# Concatenación de listas
mas_colores = colores + ["blanco", "negro", "rosa", "azul"]
mas_colores.append("naranja")
mas_colores.insert(0, "marrón")
print("\nLista ampliada (mas_colores):", mas_colores)
print("Longitud total:", len(mas_colores))
print("Antepenúltimo elemento [-3]:", mas_colores[-3])

# Operaciones de Slices (Rodajas)
print("\n--- OPERACIONES DE SLICING ---")
print("2 últimos elementos [-2:]:", mas_colores[-2:])
print("Desde el último hasta el antepenúltimo [-1:-4:-1]:", mas_colores[-1:-4:-1])
print("3 primeros [:3]:", mas_colores[:3])
print("Del segundo al cuarto [1:4]:", mas_colores[1:4])
print("Del primero al penúltimo de 2 en 2 [:-1:2]:", mas_colores[:-1:2])
print("Todos en orden inverso [::-1]:", mas_colores[::-1])
print("Todos en orden inverso de 2 en 2 [::-2]:", mas_colores[::-2])
print("Todos de 2 en 2 [::2]:", mas_colores[::2])
