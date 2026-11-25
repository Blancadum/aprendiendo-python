"""
Enunciado:
Demostración del módulo estándar 'calendar' de Python:
- Generación de calendarios anuales completos en texto con configuración de columnas y filas.
- Visualización de meses individuales.
- Cambio del día de inicio de la semana (setfirstweekday).
- Comprobación de años bisiestos (isleap).

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 12_Modulos
"""

import calendar

# Mostrar calendario anual de 2026 formateado
print("=== CALENDARIO 2026 ===")
print(calendar.calendar(2026, w=4, l=1, c=6, m=3))

# Mostrar un mes específico
print("=== DICIEMBRE 2026 ===")
print(calendar.month(2026, 12))

# Configurar el primer día de la semana en Domingo (Sunday)
calendar.setfirstweekday(calendar.SUNDAY)
print("=== DICIEMBRE 2026 (Semana inicia en Domingo) ===")
print(calendar.month(2026, 12))

# Comprobación de años bisiestos
print("¿2024 fue bisiesto?:", calendar.isleap(2024))
print("¿2026 es bisiesto?:", calendar.isleap(2026))
