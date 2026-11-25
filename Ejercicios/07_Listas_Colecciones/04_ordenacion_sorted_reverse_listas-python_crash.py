"""
Ejercicio 3-8: Ordenación de listas (sorted, reverse y sort)

Enunciado:
Crear una lista con destinos del mundo.
1. Imprimir la lista original.
2. Usar sorted() para imprimir en orden alfabético sin modificar la original.
3. Usar reverse() para invertir el orden y revertirlo de nuevo.
4. Usar sort() para modificar permanentemente la lista en orden alfabético y alfabético inverso.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 3
"""

#Lista de sitios donde me gustaría ir

locations = ["Roma", "Tokyo", "Atenas", "Viena", "Budapest"]
print ("Aquí está mi lista de sitios donde me gustaría ir: ")
print (locations)
print ("\nAquí está mi lista de sitios donde me gustaría ir ordenado alfabéticamente: ")
print (sorted(locations))
print ("\nAquí la lista sin modificar: ")
print (locations)
print ("\nAquí la lista ordenada alfabéticamente inversa: ")
print (sorted(locations, reverse=True))
print ("\nAquí la lista otra vez sin cambios: ")
print (locations)
print ("\nAquí la lista invertida con cambios permanentes: ")
locations.reverse()
print (locations)
print ("\nAhora volvemos a mostrar la lista invertida otra vez, que será como la original: ")
locations.reverse()
print (locations)
print ("\nAhora la lista ordenada alfabéticamente con cambios permanentes: ")
locations.sort()
print (locations)
print ("\nAhora la lista ordenada alfabéticamente a la inversa con cambios permanentes: ")
locations.sort(reverse=True)
print (locations)
