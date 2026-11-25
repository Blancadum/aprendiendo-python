"""
Ejercicio 10: Validación de credenciales de usuario y contraseña

Descripción:
Solicita un nombre de usuario y una contraseña con confirmación (doble entrada):
1. El nombre de usuario no puede estar vacío.
2. Las contraseñas no pueden estar vacías.
3. Ambas contraseñas deben coincidir.
Al cumplirse todas las condiciones, finaliza mostrando las credenciales registradas.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 10.- Validación de credenciales de registro con bucles while
# Requisitos:
# 1. El nombre de usuario no puede estar vacío (se repite la petición si está en blanco).
# 2. Las contraseñas no pueden estar vacías.
# 3. Ambas contraseñas deben coincidir exactamente.
# 4. Al completar el registro, muestra el usuario y la contraseña confirmada.

# 1. Solicitar nombre de usuario con bucle de validación
# 'not usuario' es True mientras la variable sea una cadena vacía ""
usuario = ""
while not usuario:
    usuario = input("Introduce un nombre de usuario: ").strip()
    if not usuario:
        print("El nombre de usuario no puede estar en blanco. Inténtalo de nuevo.")
        print()

# 2. Solicitar y validar la contraseña doble
# Bucle infinito que solo se rompe (break) cuando las credenciales son válidas
while True:
    pass1 = input("Introduce una contraseña: ")
    pass2 = input("Repite la contraseña: ")

    # Comprobación 1: Campos vacíos
    if not pass1 or not pass2:
        print("Las contraseñas no pueden estar vacías. Inténtalo de nuevo.")
        print()

    # Comprobación 2: Coincidencia
    elif pass1 != pass2:
        print("Error: Las contraseñas no coinciden. Inténtalo de nuevo.")
        print()

    # Comprobación 3: Éxito en el registro
    else:
        print()
        print("--- REGISTRO COMPLETADO CON ÉXITO ---")
        print(f"Usuario: {usuario}")
        print(f"Contraseña: {pass1}")
        break
