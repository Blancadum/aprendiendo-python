"""
Ejercicio 05: Conversión y descomposición de unidades de tiempo

Descripción:
I. Solicita al usuario los datos de días, horas y minutos, y calcula
   la cantidad total de segundos correspondientes.
II. Solicita una cantidad total de segundos y la descompone en su equivalente
    en días, horas, minutos y segundos restantes.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 05.- Conversión y descomposición de unidades de tiempo
# Parte I: Solicita días, horas y minutos y calcula el total de segundos.
# Parte II: Solicita una cantidad total de segundos y la descompone en días, horas, minutos y segundos.

# ==============================================================================
# PARTE I: Días, horas y minutos a segundos totales
# ==============================================================================
print("=== PARTE I: CONVERSIÓN A SEGUNDOS ===")

# 1. Pedir los datos al usuario y convertirlos a enteros (int)
dias = int(input("Introduce los días: "))
horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))

# 2. Calcular los segundos totales usando factores de conversión:
# 1 día = 24 horas * 3600 segundos (86400 s)
# 1 hora = 3600 segundos
# 1 minuto = 60 segundos
segundos_totales = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60)

# 3. Mostrar el total obtenido
print(f"Son un total de {segundos_totales} segundos.")
print()

# ==============================================================================
# PARTE II: Descomposición de segundos en días, horas, minutos y segundos
# ==============================================================================
print("=== PARTE II: DESCOMPOSICIÓN DE SEGUNDOS ===")

# 1. Pedir la cantidad de segundos totales
segundos_input = int(input("Introduce una cantidad de segundos: "))

# 2. Descomponer usando división entera (//) y módulo (%)
# Segundos por día: 24 * 3600 = 86400
dias_res = segundos_input // (24 * 3600)
resto = segundos_input % (24 * 3600)

# Segundos por hora: 3600
horas_res = resto // 3600
resto %= 3600

# Segundos por minuto: 60
minutos_res = resto // 60
segundos_res = resto % 60

# 3. Mostrar la descomposición final
print(f"{segundos_input} segundos equivalen a: {dias_res} días, {horas_res} horas, {minutos_res} minutos y {segundos_res} segundos.")
