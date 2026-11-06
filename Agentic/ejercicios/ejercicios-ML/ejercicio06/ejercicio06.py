"""
Blanca de Uña Martín
"""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

numeros = [num1, num2, num3]

mayor = max(numeros)
menor = min(numeros)

print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")

for n in numeros:
    if n % 2 == 0:
        print(f"El número {n} es par.")
    else:
        print(f"El número {n} es impar.")
