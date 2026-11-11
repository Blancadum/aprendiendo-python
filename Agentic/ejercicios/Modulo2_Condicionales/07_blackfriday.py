'''
    Nos preparamos para el Black Friday y estos son los descuentos: 
    - si el precio es mayor de 50 € se aplica el 10%
    - si el precio es mayor de 100 € se aplica el 20%
    solicitar el precio por teclado y mostrar el precio final
'''

precio = float(input("Introduce el precio: "))
descuento = 0

if precio > 50 and precio <= 100: 
    print("Se aplica el 10%")
    descuento = precio * 0.1
elif precio > 100:
    print("Se aplica el 20%")
    descuento = precio * 0.2
else:
    print("No se aplica descuento")

print(f"El precio inicial: {precio:.2f}, dto aplicado: {descuento:.2f}, precio final: {precio - descuento:.2f}")
