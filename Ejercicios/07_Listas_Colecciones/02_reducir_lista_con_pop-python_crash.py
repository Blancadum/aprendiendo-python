"""
Ejercicio 3-7: Reducción de lista con pop() y vaciado con del

Enunciado:
La mesa no llegará a tiempo y solo hay espacio para dos invitados.
Extraer invitados con pop() informándoles de la cancelación hasta que solo queden dos.
Confirmar la invitación a los dos restantes y finalmente vaciar la lista con del.

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

print ("Python, ¿cuántas personas hemos invitado a comer?")
print (len(guest))

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

message = "Me gustaría invitarte a cenar, " + guest[5] + "."
print (message)

print ("Python, ¿cuántas personas hemos invitado ahora a comer?")
print (len(guest))

print ("Finalmente la mesa es únicamente para dos personas, lo siento")

descartado_1 = guest.pop(0)
print (descartado_1 + " debo retirarte la invitación.")

descartado_2 = guest.pop(2)
print (descartado_2 + " debo retirarte la invitación.")

print (guest[0] + ", " + guest[1] + ", " + guest[2] + " y " + guest[3] + ", todavía estáis invitados")

print ("Python, ¿cuántas personas hemos invitado al final a comer?")
print (len(guest))

del guest[3]
del guest[2]
del guest[1]
del guest[0]

print (guest)
