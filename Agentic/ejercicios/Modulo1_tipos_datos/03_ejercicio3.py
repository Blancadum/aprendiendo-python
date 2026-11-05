'''
    Solicitar el precio de un producto
    - aplicar descuento 10%
    - aplicar 21% de IVA
    Mostrar desglose: precio inicial, importe dto, importe IVA, importe total
'''

precio_inicial = float(input("Introduce el precio del producto: "))
dto = float((precio_inicial * 10) / 100)
precio_dto = precio_inicial - dto
iva = float(precio_inicial*21/200)
precio_iva = precio_dto + iva
precio_final = precio_inicial - dto + iva
print(f"El precio inicial era de: {precio_inicial},\nhaciéndole el descuento de {dto} queda en {precio_dto},\nmás el IVA ({iva}), sería {precio_iva}.\nTotal de {precio_final} lereles")

# Forma alternativa 
