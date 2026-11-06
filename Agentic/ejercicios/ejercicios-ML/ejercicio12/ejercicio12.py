"""
Blanca de Uña Martín
"""

while True:
    n = int(input("¿Cuántos números desea imprimir? (mínimo 2 números, mayor que 2): "))
    if n > 2:
        break
    print("El número debe ser positivo y mayor que 2.")

fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

for i in range(len(fib)):
    if i == len(fib) - 1:
        print(fib[i], end="")
    else:
        print(f"{fib[i]}, ", end="")
print()
