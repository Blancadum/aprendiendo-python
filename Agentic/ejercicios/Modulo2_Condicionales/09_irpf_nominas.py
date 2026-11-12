'''
    Calcular la nómina de 2027.
'''
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