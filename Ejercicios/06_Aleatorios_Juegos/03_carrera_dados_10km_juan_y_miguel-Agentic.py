"""
Juan y Miguel participan en una carrera de 10 km.
    Cada participante avanza en km según el dado que salga
    Juan: 1 + 3 + 5 + 2 = 11
    Miguel: 6 + 1 + 4 = 11

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo6_password
"""

import random
# Marcadores iniciales de distancia recorrida
km_juan = 0
km_miguel = 0
ronda = 1
print("🏁 ¡Comienza la carrera de 10 km entre Juan y Miguel! 🏁\n")
# El bucle continúa mientras NINGUNO de los dos haya llegado a 10 km
while km_juan < 10 and km_miguel < 10:
    # Tirada de dado para cada participante (del 1 al 6)
    dado_juan = random.randint(1, 6)
    dado_miguel = random.randint(1, 6)
    # Acumulamos los km avanzados
    km_juan += dado_juan
    km_miguel += dado_miguel
    print(f"Ronda {ronda}:")
    print(f"  - Juan tira un {dado_juan}  -> Total: {km_juan} km")
    print(f"  - Miguel tira un {dado_miguel} -> Total: {km_miguel} km\n")

    ronda += 1
# Determinar el ganador al terminar la carrera
print("🏆 RESULTADO FINAL 🏆")
print(f"Juan: {km_juan} km | Miguel: {km_miguel} km\n")
if km_juan > km_miguel:
    print("¡Ha ganado Juan! 🎉")
elif km_miguel > km_juan:
    print("¡Ha ganado Miguel! 🎉")
else:
    print("¡Ha habido un empate! 🤝")
