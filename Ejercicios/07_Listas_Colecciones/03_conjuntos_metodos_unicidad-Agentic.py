"""
Enunciado:
Demostración de Conjuntos (set) en Python:
- Colecciones desordenadas (sin índices) y de elementos únicos (no admiten duplicados).
- Creación de conjuntos con llaves {} y conjunto vacío con set().
- Métodos add(), remove(), copy(), union(), clear().
- Operadores de pertenencia in y not in.
- Conversión a tupla y lista.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 9_Conjuntos
"""

frutas = {"manzana", "naranja", "pera", "naranja", "platano"}
print("Tipo:", type(frutas))
print("Contenido (los duplicados se eliminan automáticamente):", frutas)

# Creación de conjunto vacío (usar set(), ya que {} crea un dict)
conjunto_vacio = set()
print("Conjunto vacío:", conjunto_vacio, type(conjunto_vacio))

# Agregar y eliminar elementos
frutas.add("fresas")
print("Tras add('fresas'):", frutas)

frutas.remove("platano")
print("Tras remove('platano'):", frutas)

print("Número de elementos:", len(frutas))

# Unión de conjuntos
resultado = frutas.union({"melon", "sandia"})
print("Unión con {'melon', 'sandia'}:", resultado)

# Operadores de pertenencia
print("¿Está 'fresas' en frutas?:", "fresas" in frutas)
print("¿Está 'maracuyá' en frutas?:", "maracuya" in frutas)
print("¿No está 'melocotón' en frutas?:", "melocoton" not in frutas)

# Conversiones
lista_frutas = list(resultado)
tupla_frutas = tuple(resultado)
print("Convertido a lista:", lista_frutas)
print("Convertido a tupla:", tupla_frutas)

# Limpieza total
frutas.clear()
print("Tras clear():", frutas)
