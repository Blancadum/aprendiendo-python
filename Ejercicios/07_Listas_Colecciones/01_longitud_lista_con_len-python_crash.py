"""
Ejercicio 3-9: Número de invitados con len()

Enunciado:
Utilizar la función len() para contar cuántas personas están invitadas a cenar e imprimir el total.

Autor: Blanca de Uña Martín
Curso: Python Crash Course - Chapter 3
"""

guests = ["Linus", "Matt", "George"]

for guest in guests:
    print (guest +", estás invitado")

message = "Me gustaría invitarte a cenar, " + guests[0] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guests[1] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guests[2] + "."
print (message)

print ("Python, ¿cuántas personas hemos invitado a comer?")
print (len(guests))

print ("He encontrado una mesa más grande, ¡podremos invitar a más personas!")

guests.insert(0, "Richard")
guests.insert(2, "Ringo")
guests.append("Jack")

message = "Me gustaría invitarte a cenar, " + guests[0] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guests[1] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guests[2] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guests[3] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guests[4] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guests[5] + "."
print (message)

print ("Python, ¿cuántas personas hemos invitado ahora a comer?")
print (len(guests))

print ("Finalmente la mesa es únicamente para dos personas, lo siento")

descartado_1 = guests.pop(0)
print (descartado_1 + " debo retirarte la invitación.")

descartado_2 = guests.pop(2)
print (descartado_2 + " debo retirarte la invitación.")

print (guests[0] + ", " + guests[1] + ", " + guests[2] + " y " + guests[3] + ", todavía estáis invitados")

print ("Python, ¿cuántas personas hemos invitado al final a comer?")
print (len(guests))

del guests[3]
del guests[2]
del guests[1]
del guests[0]

print (guests)
