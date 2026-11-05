"""
Blanca de Uña Martín
"""

usuario = ""
while not usuario:
    usuario = input("Introduce un nombre de usuario: ")
    if not usuario:
        print("El nombre de usuario no puede estar vacío.")

while True:
    pass1 = input("Introduce una contraseña: ")
    pass2 = input("Repite la contraseña: ")
    
    if not pass1 or not pass2:
        print("Las contraseñas no pueden estar vacías.")
    elif pass1 != pass2:
        print("Error: Las contraseñas no coinciden.")
    else:
        print("¡Registro completado!")
        print(f"Usuario: {usuario}")
        print(f"Contraseña: {pass1}")
        break
