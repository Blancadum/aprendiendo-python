"""
Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo4_Bucle_for
"""

# cuando todos los elementos van entre [] es una lista
nombres = ['Luis', 'Jorge', 'Maria', 'Laura', 'Pedro']

# Mostrar todos los nombres de la lista
# Elemento es una variable que acabo de inventarme y se conoce como variable auxiliar
for elemento in nombres:
    print(elemento)

# Crear una lista de números y mostrar la suma de todos ellos
numeros = [3,8,1,5,9]
resultado = 0
for num in numeros:
    resultado += num
print("Resultado", resultado)
