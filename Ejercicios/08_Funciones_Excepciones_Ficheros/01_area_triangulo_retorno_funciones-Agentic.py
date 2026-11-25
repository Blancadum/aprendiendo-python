"""
Enunciado:
Crear una función 'area_triangulo' que reciba los argumentos necesarios
(base y altura) para calcular el área (base * altura / 2).
La función retorna el resultado y los datos se solicitan por teclado.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 6_Funciones
"""


def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2


if __name__ == "__main__":
    base_in = float(input("Introduce la base del triángulo: "))
    altura_in = float(input("Introduce la altura del triángulo: "))

    area = area_triangulo(base_in, altura_in)
    print(f"\nEl área del triángulo de base {base_in} y altura {altura_in} es: {area:.2f}")
