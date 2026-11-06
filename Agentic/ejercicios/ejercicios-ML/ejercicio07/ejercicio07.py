"""
Blanca de Uña Martín
"""

momento = input("Introduce el momento del día (m-mañana, t-tarde, n-noche): ").lower()
sexo = input("Introduce tu sexo (m-masculino, f-femenino): ").lower()

saludo_momento = ""
if momento == 'm':
    saludo_momento = "Buenos días"
elif momento == 't':
    saludo_momento = "Buenas tardes"
elif momento == 'n':
    saludo_momento = "Buenas noches"
else:
    saludo_momento = "Hola"

saludo_sexo = ""
if sexo == 'm':
    saludo_sexo = "señor"
elif sexo == 'f':
    saludo_sexo = "señora"
else:
    saludo_sexo = ""

print(f"{saludo_momento} {saludo_sexo}")
