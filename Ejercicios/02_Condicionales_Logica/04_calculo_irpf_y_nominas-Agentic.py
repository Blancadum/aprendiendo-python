"""
Enunciado:
Cálculo de la nómina y retención de IRPF para el año 2027.
El programa solicita al usuario:
- Sueldo anual bruto actual (€).
- Número de hijos.
- Porcentaje estimado de subida del IPC (%).

A partir de estos datos:
1. Calcula el sueldo bruto anual para 2027 aplicando la subida porcentual del IPC.
2. Determina el porcentaje de retención de IRPF aplicable según los tramos:
   - Sueldo bruto < 22.000 €: 5%
   - Sueldo bruto de 22.000 € a < 35.000 €: 12%
   - Sueldo bruto de 35.000 € a < 55.000 €: 20%
   - Sueldo bruto >= 55.000 €: 25%
3. Calcula el importe total retenido por IRPF y el sueldo neto anual.
4. Muestra por pantalla el desglose del sueldo bruto, porcentaje y cuantía del IRPF, y el sueldo neto final.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo2_Condicionales
"""

sueldo_actual = float(input("Introduce tu sueldo anual bruto: "))
numero_hijos = int(input("Introduce el número de hijos: "))
ipc = float(input("Introduce el IPC en porcentaje: "))

sueldo_bruto = sueldo_actual * (1 + ipc / 100)

if sueldo_bruto < 22000:
    porcentaje_irpf = 5
elif sueldo_bruto < 35000:
    porcentaje_irpf = 12
elif sueldo_bruto < 55000:
    porcentaje_irpf = 20
else:
    porcentaje_irpf = 25

irpf = sueldo_bruto * porcentaje_irpf / 100
sueldo_neto = sueldo_bruto - irpf

print(f"Sueldo bruto: {sueldo_bruto:.2f} €")
print(f"IRPF ({porcentaje_irpf}%): {irpf:.2f} €")
print(f"Sueldo neto: {sueldo_neto:.2f} €")

## También se puede imprimir todo seguido:
print(f"Tu sueldo bruto actual {sueldo_bruto:.2f} con un ipc {ipc} y un irpf del {irpf}, el sueldo bruto anual para 2027 es {sueldo_bruto:.2f}, le corresponde un sueldo neto anual para 2027 de {sueldo_neto:.2f} que corresponde a un sueldo mensual para 2027 de {sueldo_neto:.2f}€")
