"""
Blanca de Uña Martín
"""

saldo = 1000.0

while True:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            print(f"Su saldo actual es de {saldo} euros.")
        case "2":
            ingreso = float(input("¿Cuánto dinero desea ingresar?: "))
            if ingreso > 0:
                saldo += ingreso
                print(f"Ha ingresado {ingreso} euros. Nuevo saldo: {saldo} euros.")
            else:
                print("Cantidad no válida.")
        case "3":
            retiro = float(input("¿Cuánto dinero desea retirar?: "))
            if retiro > saldo:
                print("Error: No puede retirar más de lo que hay en la cuenta.")
            elif retiro > 0:
                saldo -= retiro
                print(f"Ha retirado {retiro} euros. Nuevo saldo: {saldo} euros.")
            else:
                print("Cantidad no válida.")
        case "4":
            print("Saliendo del cajero. ¡Hasta pronto!")
            break
        case _:
            print("Opción no válida. Por favor, intente de nuevo.")
