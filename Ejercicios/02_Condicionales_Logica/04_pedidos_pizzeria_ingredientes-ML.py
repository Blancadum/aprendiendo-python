"""
Ejercicio 08: Configurador de pedidos de pizzería

Descripción:
Pregunta al usuario si desea una pizza vegetariana o tradicional.
En función de su respuesta, muestra los ingredientes disponibles correspondientes
y permite elegir uno, mostrando finalmente la comanda completa con los
ingredientes base (mozzarella y tomate) más el elegido.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 08.- Configurador de pedidos de pizzería
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas.
# Todos los tipos de pizza llevan mozzarella y tomate de base.
# El cliente puede elegir además un solo ingrediente adicional entre los disponibles.

# 1. Preguntar si se desea pizza vegetariana o tradicional
tipo = input("¿Desea una pizza vegetariana? (s/n): ").lower()

# Ingredientes base comunes a todas las pizzas
ingredientes_base = ["mozzarella", "tomate"]

# 2. Ramificación condicional según la elección
if tipo == 's':
    # Menú para clientes vegetarianos
    print()
    print("Ingredientes vegetarianos disponibles: 1. Pimiento  2. Cebolla  3. Tofu")
    opcion = input("Elija un ingrediente (1, 2 o 3): ")

    if opcion == '1':
        ingrediente = "Pimiento"
    elif opcion == '2':
        ingrediente = "Cebolla"
    elif opcion == '3':
        ingrediente = "Tofu"
    else:
        ingrediente = "Ninguno"

    # Mostrar la composición de la comanda
    print()
    print("--- RESUMEN DEL PEDIDO ---")
    print("Tipo de pizza: Vegetariana")
    print(f"Ingredientes: {', '.join(ingredientes_base)}, {ingrediente}")

elif tipo == 'n':
    # Menú para clientes no vegetarianos
    print()
    print("Ingredientes disponibles: 1. Pepperoni  2. Jamón  3. Salmón")
    opcion = input("Elija un ingrediente (1, 2 o 3): ")

    if opcion == '1':
        ingrediente = "Pepperoni"
    elif opcion == '2':
        ingrediente = "Jamón"
    elif opcion == '3':
        ingrediente = "Salmón"
    else:
        ingrediente = "Ninguno"

    # Mostrar la composición de la comanda
    print()
    print("--- RESUMEN DEL PEDIDO ---")
    print("Tipo de pizza: No vegetariana")
    print(f"Ingredientes: {', '.join(ingredientes_base)}, {ingrediente}")

else:
    print("Opción no válida. Por favor, introduzca 's' para sí o 'n' para no.")
