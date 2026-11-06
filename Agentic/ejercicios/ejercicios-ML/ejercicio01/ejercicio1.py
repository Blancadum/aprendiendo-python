"""
Blanca de Uña Martín
"""

# ==============================================================================
# CREACIÓN DEL CODE-SNIPPET EN VS CODE:
# Para automatizar la inclusión del módulo 'os' y la limpieza de pantalla:
# 1. Se creó el archivo de snippets '.vscode/pyinit.code-snippets' en el proyecto.
# 2. Se definió la regla JSON con:
#    - "prefix": "pyinit" -> El atajo que se escribe en el editor.
#    - "body": Líneas de código a insertar automatizadamente (import os + os.system("clear")).
#    - "$0": Posición donde se ubica el cursor tras insertar la plantilla.
# Al escribir 'pyinit' y pulsar Tab/Enter, VS Code inserta automáticamente este bloque.
# ==============================================================================

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa "clear" para Mac/Linux y "cls" para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 01.- Ejemplo básico de Python: lectura de datos y formateo de salida

# 1. Pedir por pantalla los datos al usuario usando la función input()
# La función input() muestra la pregunta en la terminal, detiene la ejecución
# hasta que el usuario escribe un valor y lo almacena como texto (string) en la variable.
nombre = input("Introduce tu nombre: ")
primer_apellido = input("Introduce tu primer apellido: ")
segundo_apellido = input("Introduce tu segundo apellido: ")
edad = int(input("Introduce tu edad: "))
codigo_postal = input("Introduce tu código postal: ")
poblacion = input("Introduce tu población: ")
telefono = input("Introduce tu teléfono: ")

# 2. Mostrar los resultados por terminal utilizando f-strings (f"...")
# Las f-strings nos permiten formatear texto e integrar variables fácilmente mediante llaves {}
print("\n--- RESULTADOS ---")

# Concatenación de nombre y apellidos intercalando espacios
print(f"nombre completo: {nombre} {primer_apellido} {segundo_apellido}")

# Muestra el valor almacenado en la variable edad
print(f"edad: {edad}")

# Combina el código postal y la población en un formato de dirección
print(f"dirección: CP {codigo_postal}, {poblacion}")

# Muestra el número de teléfono capturado
print(f"teléfono: {telefono}")
