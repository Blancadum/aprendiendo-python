"""
Enunciado:
Demostración del módulo estándar 'datetime' para gestión de fechas, horas y deltas temporales:
- Obtención de fecha y hora actual (now, today).
- Construcción de objetos datetime con año, mes, día, hora y minutos.
- Aritmética de fechas con timedelta (sumar semanas, restar días).
- Formateo y serialización de fechas a cadenas de texto con strftime().

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 12_Modulos
"""

import datetime

# Fecha y hora actual
print("Fecha y hora actual (now):", datetime.datetime.now())
print("Fecha actual (date.today):", datetime.date.today())

# Construcción de fecha específica
fecha_hora = datetime.datetime(2027, 1, 26, 8, 30)
print("\nFecha construida:", fecha_hora)
print(f"Año: {fecha_hora.year}, Mes: {fecha_hora.month}, Día: {fecha_hora.day}")
print(f"Hora: {fecha_hora.hour}, Minutos: {fecha_hora.minute}")

# Aritmética de fechas con timedelta
delta = datetime.timedelta(weeks=1, hours=3)
print("\nDentro de una semana y 3 horas:", fecha_hora + delta)
print("Hace 2 días:", fecha_hora - datetime.timedelta(days=2))

# Formateo con strftime
print("\n--- Formateo con strftime ---")
print("Formato DD/MM/AAAA:", fecha_hora.date().strftime("%d/%m/%Y"))
print("Formato legible extendido:", fecha_hora.strftime("%A %d %B %Y"))
print("Formato con hora y minuto:", fecha_hora.strftime("%a %d %b %Y %H:%M"))
