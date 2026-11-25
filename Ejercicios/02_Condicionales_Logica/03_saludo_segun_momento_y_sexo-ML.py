"""
Ejercicio 07: Saludo condicional personalizado

Descripción:
Solicita al usuario el momento del día (m: mañana, t: tarde, n: noche)
y su sexo (m: masculino, f: femenino) para generar un saludo adecuado
(ejemplo: "Buenos días, señor", "Buenas tardes, señora").

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 07.- Generador de saludos personalizados
# Programa que pide el momento del día (mañana, tarde o noche) y el sexo
# del usuario para construir un saludo adecuado mediante condicionales.

# 1. Pedir datos y normalizar a minúsculas con el método .lower()
# .lower() asegura que funcione si el usuario introduce 'M' o 'm'
momento = input("Introduce el momento del día (m-mañana, t-tarde, n-noche): ").lower()
sexo = input("Introduce tu sexo (m-masculino, f-femenino): ").lower()

# 2. Determinar la fórmula del saludo según el momento del día
saludo_momento = ""
if momento == 'm':
    saludo_momento = "Buenos días"
elif momento == 't':
    saludo_momento = "Buenas tardes"
elif momento == 'n':
    saludo_momento = "Buenas noches"
else:
    saludo_momento = "Hola"

# 3. Determinar el tratamiento según el sexo
saludo_sexo = ""
if sexo == 'm':
    saludo_sexo = "señor"
elif sexo == 'f':
    saludo_sexo = "señora"
else:
    saludo_sexo = ""

# 4. Mostrar el saludo compuesto final
print()
print("--- SALUDO PERSONALIZADO ---")
if saludo_sexo:
    print(f"{saludo_momento}, {saludo_sexo}.")
else:
    print(f"{saludo_momento}.")
