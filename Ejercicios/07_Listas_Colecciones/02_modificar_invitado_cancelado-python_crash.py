"""
Ejercicio 3-5: Modificación de la lista de invitados

Enunciado:
Uno de los invitados no puede asistir. Imprimir quién ha cancelado, reemplazar su nombre en la lista
por un nuevo invitado y enviar una nueva ronda de invitaciones.

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

message_reject = guest[1] + " dijo: Siento no poder acudir a la cena"
print (message_reject)

guest[1] = "Jimmy"

message = "Me gustaría invitarte a cenar, " + guest[0] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[1] + "."
print (message)

message = "Me gustaría invitarte a cenar, " + guest[2] + "."
print (message)
