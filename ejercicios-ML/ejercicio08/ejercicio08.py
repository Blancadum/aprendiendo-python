"""
Blanca de Uña Martín
"""

tipo = input("¿Desea una pizza vegetariana? (s/n): ").lower()

ingredientes_base = ["mozzarella", "tomate"]

if tipo == 's':
    print("Ingredientes disponibles: 1. Pimiento 2. Cebolla 3. Tofu")
    opcion = input("Elija un ingrediente (1, 2 o 3): ")
    if opcion == '1':
        ingrediente = "Pimiento"
    elif opcion == '2':
        ingrediente = "Cebolla"
    elif opcion == '3':
        ingrediente = "Tofu"
    else:
        ingrediente = "Ninguno"
    
    print("La pizza es vegetariana.")
    print(f"Ingredientes: {', '.join(ingredientes_base)}, {ingrediente}")
    
elif tipo == 'n':
    print("Ingredientes disponibles: 1. Pepperoni 2. Jamón 3. Salmón")
    opcion = input("Elija un ingrediente (1, 2 o 3): ")
    if opcion == '1':
        ingrediente = "Pepperoni"
    elif opcion == '2':
        ingrediente = "Jamón"
    elif opcion == '3':
        ingrediente = "Salmón"
    else:
        ingrediente = "Ninguno"
        
    print("La pizza NO es vegetariana.")
    print(f"Ingredientes: {', '.join(ingredientes_base)}, {ingrediente}")
else:
    print("Opción no válida.")
