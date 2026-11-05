'''
    Solicitar 2 números enteros al usuario y mostrar el resultado de:
    suma, resta, multiplicación, división, división entera, potencia, resto de la división
'''

numero1 = input("Introduce un primer número: ")
numero2 = input("Introduce un segundo número: ")

print("La suma sería: " + str(int(numero1) + (int(numero2))))
print("La multiplicación sería: " + str(int(numero1) * (int(numero2))))
print("La resta sería: " + str(int(numero1) - (int(numero2))))
print("La división sería:" + str(int(numero1) / (int(numero2))))
print("La división entera sería: " + str(int(numero1) // (int(numero2))))
print("El módulo sería: " + str(int(numero1) % (int(numero2))))
print("La potencia sería: " + str(int(numero1)**2))

## Forma alternativa

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
division_entera = numero1 // numero2
potencia = numero1 ** numero2
resto = numero1 % numero2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Potencia: {potencia}")
print(f"Resto de la división: {resto}")

