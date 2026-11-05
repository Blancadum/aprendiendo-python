"""
Blanca de Uña Martín
"""

# Parte I
dias = int(input("Introduce los días: "))
horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))

segundos_totales = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60)
print(f"Son un total de {segundos_totales} segundos.")

# Parte II
segundos_input = int(input("Introduce una cantidad de segundos: "))
dias_res = segundos_input // (24 * 3600)
resto = segundos_input % (24 * 3600)
horas_res = resto // 3600
resto %= 3600
minutos_res = resto // 60
segundos_res = resto % 60

print(f"{segundos_input} segundos equivalen a {dias_res} días, {horas_res} horas, {minutos_res} minutos y {segundos_res} segundos.")
