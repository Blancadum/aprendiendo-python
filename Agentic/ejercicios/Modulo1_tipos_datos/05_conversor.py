'''
    Solicitar importe en euros
    Solicitar a cómo está el cambio a dolares
    Mostrar la conversión x euros son x dolares
'''

importe_euros = float(input("Introduzca el importe en euros: "))
cambio_dolares = float(input("Introduzca el cambio a dólares: "))

importe_dolares = importe_euros * cambio_dolares
print(f"{importe_euros} euros son {importe_dolares} dólares")