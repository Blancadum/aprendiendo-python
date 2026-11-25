"""
Enunciado:
Crear clase Calculadora con 4 métodos: sumar, restar, multiplicar y dividir.
Solicitar 2 números al usuario y llamar a los 4 métodos pasando los argumentos.
Mostrar los resultados por pantalla.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 14_POO
"""


# Definición de la clase Calculadora sin constructor __init__
class Calculadora:

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            return "No se puede dividir por cero"
        return num1 / num2


# 1. Solicitar 2 números al usuario
num1 = float(input("Introduce un número: "))
num2 = float(input("Introduce otro número: "))

# 2. Instanciar el objeto Calculadora (sin parámetros)
calculadora = Calculadora()

# 3. Llamar a los 4 métodos y mostrar resultados
print("\n--- RESULTADOS CALCULADORA ---")
print("Suma:", calculadora.sumar(num1, num2))
print("Resta:", calculadora.restar(num1, num2))
print("Multiplicación:", calculadora.multiplicar(num1, num2))
print("División:", calculadora.dividir(num1, num2))
