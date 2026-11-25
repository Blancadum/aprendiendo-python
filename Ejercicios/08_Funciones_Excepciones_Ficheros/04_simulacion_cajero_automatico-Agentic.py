"""
Enunciado:
Simulación interactiva de cajero automático.
El programa inicializa la cuenta con un saldo de 1000 euros y muestra un menú continuo al usuario:
1. Consultar saldo: Muestra el saldo actual disponible.
2. Ingresar dinero: Solicita la cantidad y valida que sea positiva antes de sumarla al saldo.
3. Retirar dinero: Solicita la cantidad, comprueba que sea un valor positivo y que haya saldo suficiente.
4. Salir de la aplicación: Finaliza el bucle y la ejecución del programa.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 6
"""

saldo = 1000  # Saldo inicial
while True:
    print("\n--- MENÚ CAJERO ---")
    print("1. Consultar el saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir de la aplicación")

    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        print(f"Su saldo actual es: {saldo} €")
    elif opcion == "2":
        cant = float(input("Introduce la cantidad a ingresar: "))
        if cant > 0:
            saldo += cant
            print(f"Ingreso realizado con éxito. Saldo actual: {saldo} €")
        else:
            print("La cantidad a ingresar debe ser positiva.")
    elif opcion == "3":
        cant = float(input("Introduce la cantidad a retirar: "))
        if cant <= 0:
            print("La cantidad a retirar debe ser positiva.")
        elif cant <= saldo:
            saldo -= cant
            print(f"Retirada realizada con éxito. Saldo restante: {saldo} €")
        else:
            print(f"Saldo insuficiente. Su saldo actual es solo de {saldo} €.")
    elif opcion == "4":
        print("Gracias por utilizar el cajero. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 4.")
