"""
Mostrar el menú:
        1. Piedra
        2. Papel
        3. Tijera
        El usuario elige (1-3)
    El ordenador genera un número aleatorio (1-3)

    - El papel envuelve la piedra
    - La tijera corta el papel
    - La piedra machaca la tijera

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo6_password
"""

import random
# Diccionario para traducir los números a palabras
opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
print("--- JUEGO: PIEDRA, PAPEL O TIJERA ---")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
usuario = int(input("Elige tu jugada (1-3): "))
if usuario not in [1, 2, 3]:
    print("Opción no válida. Debes elegir 1, 2 o 3.")
else:
    # El ordenador genera su tirada aleatoria (1, 2 o 3)
    ordenador = random.randint(1, 3)
    print(f"\nTú has elegido: {opciones[usuario]}")
    print(f"El ordenador ha elegido: {opciones[ordenador]}\n")
    # Evaluación del resultado
    if usuario == ordenador:
        print("¡Empate!")
    elif (usuario == 1 and ordenador == 3):
        print("¡Has ganado! La piedra machaca la tijera.")
    elif (usuario == 2 and ordenador == 1):
        print("¡Has ganado! El papel envuelve la piedra.")
    elif (usuario == 3 and ordenador == 2):
        print("¡Has ganado! La tijera corta el papel.")
    else:
# En cualquier otro caso, gana el ordenador
        if ordenador == 1 and usuario == 3:
            print("Has perdido: La piedra machaca la tijera.")
        elif ordenador == 2 and usuario == 1:
            print("Has perdido: El papel envuelve la piedra.")
        elif ordenador == 3 and usuario == 2:
            print("Has perdido: La tijera corta el papel.")
# Versión con bucle while (para seguir jugando)
# Si en clase os piden que el juego continúe hasta que el usuario decida salir (añadiendo una opción 4):

import random
opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
while True:
    print("\n--- PIEDRA, PAPEL O TIJERA ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

    usuario = int(input("Elige una opción (1-4): "))
    if usuario == 4:
        print("¡Gracias por jugar! Hasta pronto.")
        break
    if usuario not in [1, 2, 3]:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    ordenador = random.randint(1, 3)
    print(f"Tú: {opciones[usuario]} | Ordenador: {opciones[ordenador]}")
    if usuario == ordenador:
        print("-> ¡Empate!")
    elif (usuario == 1 and ordenador == 3) or \
         (usuario == 2 and ordenador == 1) or \
         (usuario == 3 and ordenador == 2):
        print("-> ¡Has ganado!")
    else:
        print("-> Ha ganado el ordenador.")
