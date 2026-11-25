"""
Enunciado:
Gestión de Stock en Almacén con Diccionarios y Funciones:
1. Crear un diccionario donde las claves sean nombres de productos y los valores sus cantidades.
2. Definir una función 'actualizar_stock' que reciba el inventario, el nombre del producto y la cantidad a sumar.
   - Si el producto ya existe, acumula la cantidad recibida.
   - Si el producto no existe, lo da de alta con esa cantidad inicial.
3. Inicializar el stock con 3 productos.
4. Ejecutar actualizaciones y mostrar el inventario formateado.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 10_Diccionarios
"""


def actualizar_stock(inventario: dict, producto: str, cantidad: int) -> dict:
    """
    Actualiza la cantidad de un producto sumándole la cantidad recibida.
    """
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    return inventario


# Stock inicial
stock_repuestos = {
    "bujías": 50,
    "pastillas de freno": 20,
    "filtros de aceite": 35,
}

print("=== STOCK INICIAL ===")
for prod, cant in stock_repuestos.items():
    print(f"Producto: {prod:<20} | Unidades: {cant}")

# Actualizaciones
actualizar_stock(stock_repuestos, "bujías", 30)  # Producto existente
actualizar_stock(stock_repuestos, "líquido de frenos", 15)  # Producto nuevo

print("\n=== STOCK ACTUALIZADO ===")
for prod, cant in stock_repuestos.items():
    print(f"Producto: {prod:<20} | Unidades: {cant}")
