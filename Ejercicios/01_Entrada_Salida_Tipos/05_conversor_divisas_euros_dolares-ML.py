"""
Ejercicio 03: Conversor de divisas (Euros y Dólares)

Descripción:
Suponiendo que 1 euro = 1.33250 dólares, escribe un programa que pida al usuario
un número de dólares y calcule el cambio en euros redondeando a dos decimales.
Posteriormente, pedirá un número de euros y calculará el cambio en dólares
redondeando a dos decimales.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 03.- Conversor de divisas (Dólares <-> Euros)
# Tasa de cambio de referencia: 1 Euro = 1.33250 Dólares
# El programa pide una cantidad en dólares y la convierte a euros,
# y a continuación pide una cantidad en euros y la convierte a dólares.

# Constante con la tasa de cambio fija
TASA_CAMBIO = 1.33250

# 1. Conversión de Dólares a Euros
# Pedimos la cantidad en dólares mediante float() para admitir decimales
dolares = float(input("Introduce la cantidad de dólares: "))

# Para pasar de dólares a euros dividimos entre la tasa de cambio
euros = dolares / TASA_CAMBIO

# Mostramos el resultado redondeado a 2 decimales con round()
print(f"El cambio es {round(euros, 2)} euros.")
print()

# 2. Conversión de Euros a Dólares
# Pedimos la cantidad en euros
euros_usuario = float(input("Introduce la cantidad de euros: "))

# Para pasar de euros a dólares multiplicamos por la tasa de cambio
dolares_usuario = euros_usuario * TASA_CAMBIO

# Mostramos el resultado redondeado a 2 decimales con round()
print(f"El cambio es {round(dolares_usuario, 2)} dólares.")
