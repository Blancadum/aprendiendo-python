"""
Enunciado:
Crear una función 'calcular_precio' que recibe el precio del producto
y el porcentaje de descuento opcional (por defecto 10%).
Retornar el precio final tras aplicar la rebaja.
Probar con diferentes precios y descuentos.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 6_Funciones
"""


def calcular_precio(precio: float, porcentaje_descuento: float = 10.0) -> float:
    descuento = precio * (porcentaje_descuento / 100)
    return precio - descuento


if __name__ == "__main__":
    # Prueba 1: 100€ con 10% por defecto
    p1 = 100.0
    print(f"Precio: {p1}€ | Descuento defecto: 10% -> Final: {calcular_precio(p1):.2f}€")

    # Prueba 2: 50€ con 20%
    p2 = 50.0
    dto2 = 20.0
    print(f"Precio: {p2}€ | Descuento: {dto2}% -> Final: {calcular_precio(p2, dto2):.2f}€")

    # Prueba 3: 200€ sin descuento (0%)
    p3 = 200.0
    print(f"Precio: {p3}€ | Descuento: 0% -> Final: {calcular_precio(p3, 0):.2f}€")
