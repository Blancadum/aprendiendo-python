"""
Blanca de Uña Martín
"""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
letra = input("Introduce 'p' para pares o 'i' para impares: ").lower()

inicio = min(num1, num2)
fin = max(num1, num2)

if letra == 'p':
    for i in range(inicio, fin + 1):
        if i % 2 == 0:
            print(i)
elif letra == 'i':
    for i in range(inicio, fin + 1):
        if i % 2 != 0:
            print(i)
