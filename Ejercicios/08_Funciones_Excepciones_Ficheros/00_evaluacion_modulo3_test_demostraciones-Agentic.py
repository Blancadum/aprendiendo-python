"""
Enunciado:
Evaluación Módulo 3 - Test con Demostraciones Prácticas de Código:
1. Retorno por defecto de una función sin sentencia 'return' explícita (devuelve None).
2. Diferencia entre lista y tupla (mutabilidad vs inmutabilidad).
3. Sintaxis de definición de funciones ('def').
4. Diccionarios (estructura clave: valor).
5. Conjuntos (elementos únicos y desordenados).

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 6_Funciones
"""


# 1. Retorno por defecto
def funcion_sin_return():
    pass


resultado = funcion_sin_return()
print("1. Retorno por defecto de función sin return:", resultado)  # None

# 2. Mutabilidad de lista vs tupla
lista = [1, 2, 3]
tupla = (1, 2, 3)
lista[0] = 99  # Permitido
print("2. Lista mutable:", lista)
# tupla[0] = 99 -> TypeError: 'tuple' object does not support item assignment

# 3. Definición de función
print("3. Definición de función realizada con éxito mediante 'def'.")

# 4. Diccionarios clave-valor
inventario = {"manzanas": 10, "peras": 5}
print("4. Diccionario clave-valor:", inventario)

# 5. Conjunto sin duplicados
conjunto = {1, 2, 2, 3, 3, 3}
print("5. Conjunto único:", conjunto)
