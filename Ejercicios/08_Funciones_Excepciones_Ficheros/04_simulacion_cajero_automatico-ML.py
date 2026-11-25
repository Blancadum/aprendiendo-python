"""
Ejercicio 09: Simulación de cajero automático (Match-Case)

Descripción:
Simula un cajero automático con un saldo inicial de 1000 euros mediante un menú
interactivo continuo usando la estructura match/case:
1. Consultar saldo.
2. Ingresar dinero (suma al saldo).
3. Retirar dinero (valida fondos suficientes).
4. Salir de la aplicación.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 09.- Simulación de cajero automático (Match-Case)
# Saldo inicial de 1000 euros.
# Menú continuo con 4 opciones usando la estructura 'match / case':
# 1. Consultar saldo
# 2. Ingresar dinero
# 3. Retirar dinero (validando que haya saldo suficiente)
# 4. Salir

# 1. Definición del saldo inicial
saldo = 1000.0

# 2. Bucle infinito while True para mantener activo el menú del cajero
while True:
    print()
    print("--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")

    # 3. Evaluación de opciones mediante match / case
    match opcion:
        case "1":
# Consulta directa del saldo actual
            print(f"Su saldo actual es de {saldo:.2f} euros.")

        case "2":
# Ingreso de dinero: validamos que la cantidad sea positiva
            ingreso = float(input("¿Cuánto dinero desea ingresar?: "))
            if ingreso > 0:
                saldo += ingreso
                print(f"Ha ingresado {ingreso:.2f} euros. Nuevo saldo: {saldo:.2f} euros.")
            else:
                print("Cantidad no válida. El importe debe ser mayor que 0.")

        case "3":
# Retirada de efectivo: validamos fondos suficientes
            retiro = float(input("¿Cuánto dinero desea retirar?: "))
            if retiro > saldo:
                print(f"Error: Fondos insuficientes. Su saldo disponible es {saldo:.2f} euros.")
            elif retiro > 0:
                saldo -= retiro
                print(f"Ha retirado {retiro:.2f} euros. Nuevo saldo: {saldo:.2f} euros.")
            else:
                print("Cantidad no válida. El importe debe ser mayor que 0.")

        case "4":
# Salir de la aplicación rompiendo el bucle con break
            print("Saliendo del cajero. ¡Gracias por su visita!")
            break

        case _:
# Caso comodín para cualquier opción que no coincida con 1-4
            print("Opción no válida. Por favor, introduzca un número del 1 al 4.")
