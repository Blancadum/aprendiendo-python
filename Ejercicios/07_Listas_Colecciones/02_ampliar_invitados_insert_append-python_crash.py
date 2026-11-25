"""
Ejercicio 3-6: Ampliación de la mesa de invitados (insert y append)

Enunciado:
Se dispone de una mesa más grande. Añadir un invitado al inicio con insert(0, ...),
otro en la posición intermedia con insert(len//2, ...) y otro al final con append().
Imprimir las nuevas invitaciones.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 3
"""

guest = ["Linus", "Matt", "George"]

message = "Me gustaría invitarte a cenar, " + guest[0] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[1] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[2] + "."
print (message)

print ("He encontrado una mesa más grande, ¡podremos invitar a más personas!")

guest.insert(0, "Richard")
guest.insert(2, "Ringo")
guest.append("Jack")

message = "Me gustaría invitarte a cenar, " + guest[0] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[1] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[2] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[3] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[4] + "."
print (message)
