"""
Enunciado:
Calculadora modularizada con funciones y validación:
- Solicitar 2 números al usuario y ejecutar las 4 operaciones básicas.
- Diseñar 5 funciones:
  * sumar(n1, n2)
  * restar(n1, n2)
  * multiplicar(n1, n2)
  * dividir(n1, n2)
  * validar_divisor(divisor) -> Devuelve True si es distinto de cero, False en caso contrario.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 6_Funciones
"""


def sumar(n1: float, n2: float) -> float:
    return n1 + n2


def restar(n1: float, n2: float) -> float:
    return n1 - n2


def multiplicar(n1: float, n2: float) -> float:
    return n1 * n2


def validar_divisor(divisor: float) -> bool:
    return divisor != 0


def dividir(n1: float, n2: float) -> None:
    if validar_divisor(n2):
        res = n1 / n2
        print(f"{n1} / {n2} = {res:.2f}")
    else:
        print("Lo siento, no puedo hacer la división (divisor no puede ser cero).")


if __name__ == "__main__":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print(f"\nSuma: {a} + {b} = {sumar(a, b)}")
    print(f"Resta: {a} - {b} = {restar(a, b)}")
    print(f"Multiplicación: {a} * {b} = {multiplicar(a, b)}")
    print("División:", end=" ")
    dividir(a, b)
