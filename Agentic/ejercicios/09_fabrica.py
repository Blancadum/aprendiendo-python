'''
    Una fábrica produce 350 productos al día
    - Aumenta la producción en 125 unidades
    - Reduce la producción en 75 unidades
    - Duplica la producción *2
    - Divide entre 5
    - Cuántas sobran respecto a la producción media por día
    Calcular cuántas unidades sobran al agrupar la producción en lotes de 12 unidades
'''

produccion = 350
produccion += 125
produccion -= 75
produccion *= 2
produccion /= 5
produccion %= 12
print(f"Unidades sobrantes {produccion}")