"""
Enunciado:
Introducción a la definición y llamada de funciones en Python:
- Tipado opcional de variables y funciones (type hints).
- Funciones sin retorno (retornan None implícitamente).
- Funciones con retorno (return).
- Funciones con argumentos posicionales obligatorios y con valores por defecto.
- Invocación de funciones y captura de sus valores de retorno.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 6_Funciones
"""


# Función sin retorno (retorna None)
def saludar() -> None:
    print("Buenas tardes")


# Función con retorno tipo str
def despedir() -> str:
    return "Hasta luego"


# Función con argumentos posicionales
def presentacion(nombre: str, edad: int) -> str:
    return f"Hola, me llamo {nombre} y tengo {edad} años."


# Función con argumento con valor por defecto
def calcular_descuento(precio: float, porcentaje: float = 10.0) -> float:
    return precio * (1 - porcentaje / 100)


if __name__ == "__main__":
    saludar()
    mensaje = despedir()
    print("Retorno de despedir():", mensaje)

    ficha = presentacion("Blanca", 25)
    print(ficha)

    print("Precio con descuento por defecto (10%):", calcular_descuento(100))
    print("Precio con descuento personalizado (25%):", calcular_descuento(100, 25))
